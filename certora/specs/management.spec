import "./alwaysRevert.spec";

methods {
    function balanceOf(address) external returns (uint256) envfree;

    // optimizations
    function _emitUserOperationEvent(EntryPoint.UserOpInfo memory opInfo, bool success, uint256 actualGasCost, uint256 actualGas) internal => NONDET;
    function _emitPrefundTooLow(EntryPoint.UserOpInfo memory opInfo) internal => NONDET;
    function Exec.getReturnData(uint256) internal returns (bytes memory) => nondetBytes();
    function _callValidatePaymasterUserOp(
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

definition THEORETICAL_MAX_ETH_SUPPLY() returns uint = 300 * 10^6 * 10^18; // 300 million ETH

ghost mapping(address => uint256) mirrorDeposits {
    init_state axiom forall address u. mirrorDeposits[u] == 0;
}

hook Sstore currentContract.deposits[KEY address a].deposit uint256 newVal {
    mirrorDeposits[a] = newVal;
}

hook Sload uint256 val currentContract.deposits[KEY address a].deposit {
    require mirrorDeposits[a] == val;
}

strong invariant eachDepositLessThanMaxEthSupply()
    forall address u. mirrorDeposits[u] <= (sum address a. mirrorDeposits[a])
filtered { f -> !alwaysReverting(f) } {
    preserved with (env e) {
        requireInvariant depositsLessThanMaxEthSupply();
    }
}

strong invariant depositsLessThanMaxEthSupply()
    (sum address a. mirrorDeposits[a]) <= THEORETICAL_MAX_ETH_SUPPLY()
filtered { f -> !alwaysReverting(f) } {
    preserved with (env e) {
        requireInvariant eachDepositLessThanMaxEthSupply();
    }
}

hook CALLVALUE uint256 value {
    require value < THEORETICAL_MAX_ETH_SUPPLY();
}

//// # Validity of balance decrease
rule onlySelfReduces(method f, address user) 
filtered { f -> !alwaysReverting(f) }
{
    requireInvariant depositsLessThanMaxEthSupply();
    requireInvariant eachDepositLessThanMaxEthSupply();
    env e;
    calldataarg args;
    uint256 before =  balanceOf(user);
    require (sum address a. mirrorDeposits[a]) + e.msg.value <= THEORETICAL_MAX_ETH_SUPPLY();
    f(e, args);
    uint256 after =  balanceOf(user);
    assert after < before => e.msg.sender == user;
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
	saw_failing_call = saw_failing_call || rc == 0;
}

rule failing_CALL_leads_to_revert(method f) 
filtered { f -> f.selector != sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector }
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


//// # Advanced multi-parametric rules

rule noFrontRunning(method f, method g) 
filtered { f -> !alwaysReverting(f), g -> !alwaysReverting(g) } 
{
    env eF;
    env eG;
    calldataarg cF;
    calldataarg cG;

    storage initialStorage = lastStorage;
    f(eF, cF);

    g(eG, cG) at initialStorage;
    f@withrevert(eF, cF);
    bool succeeded = !lastReverted;

    assert succeeded, "function f is front-runnable by function g";
}

rule noUnfairGainInSameBlock(method f, method g) 
filtered { f -> !alwaysReverting(f), g -> !alwaysReverting(g) } 
{
    env eF;
    env eG;
    calldataarg cF;
    calldataarg cG;

    require eF.block.timestamp == eG.block.timestamp;
    require eF.block.number == eG.block.number;

    storage initialStorage = lastStorage;
    f@withrevert(eF, cF);
    bool fFailedFirstTime = lastReverted;
    require fFailedFirstTime;

    g(eG, cG) at initialStorage;
    f@withrevert(eF, cF);
    bool fFailedSecondTime = lastReverted;

    assert fFailedSecondTime, "function f can be made to succeed in same block by calling g";
}