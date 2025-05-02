import "./alwaysRevert.spec";

methods {
    function balanceOf(address) external returns (uint256) envfree;

    // optimizations
    function EntryPoint._emitUserOperationEvent(EntryPoint.UserOpInfo memory opInfo, bool success, uint256 actualGasCost, uint256 actualGas) internal => NONDET;
    function EntryPoint._emitPrefundTooLow(EntryPoint.UserOpInfo memory opInfo) internal => NONDET;
    function Exec.getReturnData(uint256) internal returns (bytes memory) => nondetBytes();
    function EntryPoint._callValidatePaymasterUserOp(
        uint256 opIndex,
        EntryPoint.PackedUserOperation calldata op,
        EntryPoint.UserOpInfo memory opInfo) internal returns (bytes memory, uint256) => cvlCallValidatePaymasterUserOp(opIndex, op, opInfo, executingContract);

}

function nondetBytes() returns bytes {
    bytes b;
    return b;
}

function cvlCallValidatePaymasterUserOp(uint256 opIndex, EntryPoint.PackedUserOperation op, EntryPoint.UserOpInfo opInfo, address executing) returns (bytes, uint256) {
    bytes context;
    uint256 validationData;
    return (context, validationData);
}

definition coreOperations(method f) returns bool = 
    f.selector == sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector
    || f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector
    || f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector;

definition THEORETICAL_MAX_ETH_SUPPLY() returns uint = 300 * 10^6 * 10^18; // 300 million ETH

ghost mathint sumDeposits {
    init_state axiom sumDeposits == 0;
    axiom sumDeposits >= 0;
}

ghost mathint sumStakes {
    init_state axiom sumStakes == 0;
    axiom sumStakes >= 0;
}

ghost mapping(address => uint256) mirrorDeposits {
    init_state axiom forall address u. mirrorDeposits[u] == 0;
}

ghost mapping(address => uint112) mirrorStakes {
    init_state axiom forall address u. mirrorStakes[u] == 0;
}

hook Sstore currentContract.deposits[KEY address a].deposit uint256 newVal (uint256 oldVal) {
    sumDeposits = sumDeposits + newVal - oldVal;
    mirrorDeposits[a] = newVal;
}

hook Sstore currentContract.deposits[KEY address a].stake uint112 newVal (uint112 oldVal) {
    sumStakes = sumStakes + newVal - oldVal;
    mirrorStakes[a] = newVal;
}

hook Sload uint256 val currentContract.deposits[KEY address a].deposit {
    require sumDeposits >= val;
    require mirrorDeposits[a] == val;
}

hook Sload uint112 val currentContract.deposits[KEY address a].stake {
    require sumStakes >= val;
    require mirrorStakes[a] == val;
}

strong invariant depositsAndStakesLessThanMaxEthSupply()
    sumDeposits + sumStakes <= THEORETICAL_MAX_ETH_SUPPLY()
filtered { f -> !alwaysReverting(f) && !coreOperations(f) } {
    preserved with (env e) {
        require forall address u. mirrorDeposits[u] <= sumDeposits;
        require forall address u. mirrorStakes[u] <= sumStakes;
        require e.msg.value + sumDeposits + sumStakes <= THEORETICAL_MAX_ETH_SUPPLY();
    }
}

hook CALLVALUE uint256 value {
    require value < THEORETICAL_MAX_ETH_SUPPLY();
}

//// # Deposit-related rules
//// ## Validity of deposit decrease
rule onlySelfReduces(method f, address user) 
filtered { f -> !alwaysReverting(f) && !coreOperations(f) }
{
    requireInvariant depositsAndStakesLessThanMaxEthSupply();
    require forall address u. mirrorDeposits[u] <= sumDeposits;
    env e;
    calldataarg args;
    uint256 before =  balanceOf(user);
    require sumDeposits + e.msg.value <= THEORETICAL_MAX_ETH_SUPPLY();
    f(e, args);
    uint256 after =  balanceOf(user);
    assert after < before => e.msg.sender == user;
}

//// ## Can always withdraw deposits up to max, if receiver does not reject the funds
rule withdrawalMustSucceed() {
    address to;
    uint256 amount;

    env e;
    withdrawTo@withrevert(e, to, amount);
    bool succeeded = !lastReverted;

    assert (amount <= currentContract.deposits[e.msg.sender].deposit && e.msg.value == 0 && !saw_failing_call) => succeeded;
}

//// ## Withdrawals are additive and right amounts are withdrawn
rule withdrawalIsAdditive(bool direction) {
    requireInvariant depositsAndStakesLessThanMaxEthSupply();
    require forall address u. mirrorDeposits[u] <= sumDeposits;

    env e1;
    address to1;
    uint256 amount1;
    env e2;
    address to2;
    uint256 amount2;
    env e3;
    address to3;
    uint256 amount3;

    address user;
    require e1.msg.sender == user;
    require e2.msg.sender == user; 
    require e3.msg.sender == user;

    bool isEntryPoint = user == currentContract; /* weird edge cases happen if the EntryPoint could withdraw */

    uint256 initialDeposit = currentContract.deposits[user].deposit;

    storage init = lastStorage;
    uint256 finalDeposit1;
    uint256 finalDeposit2;
    bool succeeded;
    if (direction) {
        withdrawTo(e1, to1, amount1);
        withdrawTo(e2, to2, amount2);
        finalDeposit1 = currentContract.deposits[user].deposit;
        assert !isEntryPoint => initialDeposit-finalDeposit1 == amount1+amount2;

        withdrawTo@withrevert(e3, to3, amount3) at init;
        succeeded = !lastReverted;
        finalDeposit2 = currentContract.deposits[user].deposit;
        assert (succeeded && !isEntryPoint) => initialDeposit-finalDeposit2 == amount3;
    } else {
        withdrawTo(e3, to3, amount3) ;
        finalDeposit1 = currentContract.deposits[user].deposit;
        assert !isEntryPoint => initialDeposit-finalDeposit1 == amount3;

        withdrawTo@withrevert(e1, to1, amount1) at init;
        bool succeeded1 = !lastReverted;
        withdrawTo@withrevert(e2, to2, amount2);
        succeeded = succeeded1 && !lastReverted;
        finalDeposit2 = currentContract.deposits[user].deposit;
        assert (succeeded && !isEntryPoint) => initialDeposit-finalDeposit2 == amount1+amount2;

    }

    assert !isEntryPoint => (amount3 == amount1+amount2 && e1.msg.value == 0 && e2.msg.value == 0 && e3.msg.value == 0 && !saw_failing_call) => succeeded;
    assert succeeded => amount3 <= initialDeposit;
}

//// # Stake-related rules
//// ## Can only change own's stake
rule onlySelfCanChangeStake(method f, address user)
filtered { f -> !alwaysReverting(f) }
{
    env e;
    calldataarg args;
    uint256 before = currentContract.deposits[user].stake;
    f(e, args);
    uint256 after = currentContract.deposits[user].stake;
    assert after != before => e.msg.sender == user;
}

//// ## Unstake delay is monotone inc (unless withdrawn)
rule unstakeDelayIsMonotoneInc(method f, address user)
filtered { f -> !alwaysReverting(f) }
{
    env e;
    calldataarg args;

    uint256 before = currentContract.deposits[user].unstakeDelaySec;
    f(e, args);
    uint256 after = currentContract.deposits[user].unstakeDelaySec;

    assert after >= before || (f.selector == sig:withdrawStake(address).selector && e.msg.sender == user && after == 0);
}

//// ## Cannot withdraw before time
rule cannotWithdrawBeforeTime(method f, address user)
filtered { f -> !alwaysReverting(f) }
{
    mathint origDelay = currentContract.deposits[user].unstakeDelaySec;

    env eUnlock;
    
    require eUnlock.msg.sender == user;
    require eUnlock.block.timestamp <= max_uint48; // contract assumed 48 bit bound for timestamp
    unlockStake(eUnlock);

    mathint unlockTime = eUnlock.block.timestamp;

    env eF;
    require eF.block.timestamp >= eUnlock.block.timestamp;
    calldataarg args;
    f(eF, args);

    env eWithdraw;
    require eWithdraw.msg.sender == user;
    require eWithdraw.block.timestamp >= eF.block.timestamp;
    address recipient;
    withdrawStake@withrevert(eWithdraw, recipient);
    bool success = !lastReverted;

    assert success => eWithdraw.block.timestamp >= unlockTime + origDelay;
}


//// ## stake > 0 iff unstakeDelaySec > 0
invariant stakePositiveIffUnstakeDelayIsPositive(address a)
    currentContract.deposits[a].stake > 0 <=> currentContract.deposits[a].unstakeDelaySec > 0
filtered { f -> !alwaysReverting(f) }

/**
 * State no-stake: stake == 0, unstakeDelaySec == 0, staked == false, withdrawTime == 0
 * State locked: stake > 0, unstakeDelaySec > 0, staked == true, withdrawTime == 0
 * State unlocked pending: stake > 0, unstakeDelaySec > 0, staked == false, withdrawTime > 0
 */
function isNoStakeState(address a) returns bool { return (currentContract.deposits[a].stake == 0 && currentContract.deposits[a].unstakeDelaySec == 0 && currentContract.deposits[a].staked == false && currentContract.deposits[a].withdrawTime == 0); }

function isLockedStakeState(address a) returns bool { return (currentContract.deposits[a].stake > 0 && currentContract.deposits[a].unstakeDelaySec > 0 && currentContract.deposits[a].staked == true && currentContract.deposits[a].withdrawTime == 0); }

function isUnlockedPendingState(address a) returns bool { return (currentContract.deposits[a].stake > 0 && currentContract.deposits[a].unstakeDelaySec > 0 && currentContract.deposits[a].staked == false && currentContract.deposits[a].withdrawTime > 0); }

invariant validStatesOfStake(address a)
    isNoStakeState(a)
    || isLockedStakeState(a)
    || isUnlockedPendingState(a)
filtered { f -> !alwaysReverting(f) }

rule validTransition(method f, address a) 
filtered { f -> !alwaysReverting(f) }
{
    requireInvariant validStatesOfStake(a);

    bool origIsNoStake = isNoStakeState(a);
    bool origIsLocked = isLockedStakeState(a);
    bool origIsUnlockedPending = isUnlockedPendingState(a);

    // sanity checks - just one state
    assert origIsNoStake => !origIsLocked && !origIsUnlockedPending;
    assert origIsLocked => !origIsNoStake && !origIsUnlockedPending;
    assert origIsUnlockedPending => !origIsNoStake && !origIsLocked;

    env e;
    calldataarg args;
    f(e, args);

    bool newIsNoStake = isNoStakeState(a);
    bool newIsLocked = isLockedStakeState(a);
    bool newIsUnlockedPending = isUnlockedPendingState(a);

    // transitions from NoStake:
    assert origIsNoStake && newIsLocked => f.selector == sig:addStake(uint32).selector;
    assert !(origIsNoStake && newIsUnlockedPending); // impossible

    // transitions from Locked:
    assert origIsLocked && newIsUnlockedPending => f.selector == sig:unlockStake().selector;
    assert !(origIsLocked && newIsNoStake);

    // transitions from UnlockedPending:
    assert origIsUnlockedPending && newIsLocked => f.selector == sig:addStake(uint32).selector;
    assert origIsUnlockedPending && newIsNoStake => f.selector == sig:withdrawStake(address).selector;

    // which transitions can occur as a result of each method
    if (e.msg.sender == a) {
        assert f.selector == sig:addStake(uint32).selector => 
            (origIsNoStake && newIsLocked) // adding stake moving to locked
            || (origIsLocked && newIsLocked) // staying locked
            || (origIsUnlockedPending && newIsLocked) // back to locked by adding stake
            ;
        assert f.selector == sig:unlockStake().selector => (origIsLocked && newIsUnlockedPending);
        assert f.selector == sig:withdrawStake(address).selector => (origIsUnlockedPending && newIsNoStake);
    } else {
        assert origIsNoStake => newIsNoStake;
        assert origIsLocked => newIsLocked;
        assert origIsUnlockedPending => newIsUnlockedPending;
    }
}

//// # Validate only the EntryPoint can invoke `innerHandleOp`
rule innerHandleOpProtected()
{
    env e;
    bytes callData;
    EntryPoint.UserOpInfo opInfo;
    bytes context;
    require e.msg.sender != currentContract;

    innerHandleOp@withrevert(e, callData, opInfo, context);
    assert lastReverted;
}

//// # Generic rules

/* failing CALL should lead to a revert */
persistent ghost bool saw_failing_call;

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc {
    // not entirely sound, but we want to make it more deterministic for repeated fallback calls
    if (selector == 0) {
        require rc == rcModel[addr];
    }

    bool isInnerHandleOp = selector == sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector; // not checked on purpose
	saw_failing_call = saw_failing_call || (rc == 0 && !isInnerHandleOp);
}

persistent ghost mapping(address => uint) rcModel;

rule failing_CALL_leads_to_revert(method f) 
filtered { f -> f.selector != sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector /* postOp and Exec.call not checked, on purpose */}
{
	saw_failing_call = false;
	env e;
	calldataarg arg;
	f@withrevert(e, arg);
	bool reverted = lastReverted;
	assert saw_failing_call => reverted;
}

use builtin rule hasDelegateCalls filtered { f -> f.selector != sig:delegateAndRevert(address,bytes).selector }
use builtin rule msgValueInLoopRule;
use builtin rule sanity filtered { f -> !alwaysReverting(f) }

use rule alwaysRevert;

//// # Advanced multi-parametric rules

rule noFrontRunning(method f, method g) 
filtered { f -> !alwaysReverting(f) && !coreOperations(f) && !f.isView , g -> !alwaysReverting(g) && !coreOperations(g) && !g.isView } 
{
    requireInvariant depositsAndStakesLessThanMaxEthSupply();
    require forall address u. mirrorDeposits[u] <= sumDeposits;
    env eF;
    env eG;
    calldataarg cF;
    address beneficiaryF; // for withdraw functions
    uint256 amtF; // for withdrawTo
    calldataarg cG;

    storage initialStorage = lastStorage;
    if (f.selector == sig:withdrawTo(address,uint256).selector) {
        withdrawTo(eF, beneficiaryF, amtF);
    } else if (f.selector == sig:withdrawStake(address).selector) {
        withdrawStake(eF, beneficiaryF);
    } else {
        f(eF, cF);
    }

    g(eG, cG) at initialStorage;
    if (f.selector == sig:withdrawTo(address,uint256).selector) {
        withdrawTo@withrevert(eF, beneficiaryF, amtF);
    } else if (f.selector == sig:withdrawStake(address).selector) {
        withdrawStake@withrevert(eF, beneficiaryF);
    } else {
        f@withrevert(eF, cF);
    }
    bool succeeded = !lastReverted;

    require eF.msg.sender != eG.msg.sender; // only interesting if another user front-runs us
    // We know that having the entrypoint call functions leads to weird behaviors already
    require eF.msg.sender != currentContract; 
    require eG.msg.sender != currentContract;
    require beneficiaryF != currentContract;
    assert succeeded, "function f is front-runnable by function g";
}

rule noUnfairGainInSameBlock(method f, method g) 
filtered { f -> !alwaysReverting(f) && !coreOperations(f) && !f.isView , g -> !alwaysReverting(g) && !coreOperations(g) && !g.isView  } 
{
    env eF;
    env eG;
    calldataarg cF;
    address beneficiaryF; // for withdraw functions
    uint256 amtF; // for withdrawTo
    uint32 unstakeDelaySecF; // for addStake
    calldataarg cG;

    requireInvariant depositsAndStakesLessThanMaxEthSupply();
    require forall address u. mirrorDeposits[u] <= sumDeposits;
    requireInvariant validStatesOfStake(eF.msg.sender);

    // same block assumption, part of rule definition
    require eF.block.timestamp == eG.block.timestamp;
    require eF.block.number == eG.block.number;
    require eF.block.timestamp <= max_uint48; // contract assumed 48 bit bound for timestamp

    storage initialStorage = lastStorage;
    uint256 origBalance = nativeBalances[eF.msg.sender];
    uint256 origDeposit = currentContract.deposits[eF.msg.sender].deposit;
    uint32 origUnstakeDelaySec = currentContract.deposits[eF.msg.sender].unstakeDelaySec;
    bool origStaked = currentContract.deposits[eF.msg.sender].staked;
    if (f.selector == sig:withdrawTo(address,uint256).selector) {
        withdrawTo@withrevert(eF, beneficiaryF, amtF);
    } else if (f.selector == sig:withdrawStake(address).selector) {
        withdrawStake@withrevert(eF, beneficiaryF);
    } else if (f.selector == sig:addStake(uint32).selector) {
        addStake@withrevert(eF, unstakeDelaySecF);
    } else {
        f@withrevert(eF, cF);
    }
    bool fFailedFirstTime = lastReverted;
    require fFailedFirstTime;

    g(eG, cG) at initialStorage;
    if (f.selector == sig:withdrawTo(address,uint256).selector) {
        withdrawTo@withrevert(eF, beneficiaryF, amtF);
    } else if (f.selector == sig:withdrawStake(address).selector) {
        withdrawStake@withrevert(eF, beneficiaryF);
    } else if (f.selector == sig:addStake(uint32).selector) {
        addStake@withrevert(eF, unstakeDelaySecF);
    } else {
        f@withrevert(eF, cF);
    }
    bool fFailedSecondTime = lastReverted;

    // We know that having the entrypoint call functions leads to weird behaviors already
    require eF.msg.sender != currentContract; 
    require eG.msg.sender != currentContract;
    // if we are trying to add stake, we cannot expect to front-run adding a 0 stake by adding stake...
    require f.selector == sig:addStake(uint32).selector => eF.msg.value > 0 || g.selector != sig:addStake(uint32).selector;
    // if we are trying to add stake, let's assume we had enough balance to begin with, front-running by withdrawing/getting more money is not interesting
    require f.selector == sig:addStake(uint32).selector => eF.msg.value <= origBalance;
    // similar for depositTo
    require f.selector == sig:depositTo(address).selector => eF.msg.value <= origBalance;
    // withdrawTo can succeed but we need to deposit first, this is trivial
    require (f.selector == sig:withdrawTo(address,uint256).selector && amtF > origDeposit) => (g.selector != sig:depositTo(address).selector && !g.isFallback);
    // similarly, to unlock stake one needs to add it first
    require (f.selector == sig:unlockStake().selector && (!origStaked || origUnstakeDelaySec == 0)) => g.selector != sig:addStake(uint32).selector;
    // similarly, you cannot add stake with a lower unstake delay before you withdrew the former stake
    require (f.selector == sig:addStake(uint32).selector && unstakeDelaySecF < origUnstakeDelaySec) => g.selector != sig:withdrawStake(address).selector;
    assert fFailedSecondTime, "function f can be made to succeed in same block by calling g";
}