import "./management.spec";

methods {
    function _.createSender(bytes initCode) external => NONDET;
    function _.initEip7702Sender(
        address sender,
        bytes initCode
    ) external => NONDET;
    function _.validateUserOp(
        EntryPoint.PackedUserOperation userOp,
        bytes32 hash,
        uint256 missingFunds
    ) external => NONDET;
    function _.postOp(IPaymaster.PostOpMode,bytes,uint256,uint256) external => NONDET;
    unresolved external in _._ => DISPATCH [] default NONDET;
}

//// ## Core operations do not touch deposits
rule coreOperationsDoNotTouchDeposits(method f)
filtered { f -> coreOperations(f) }
{
    requireInvariant depositsAndStakesLessThanMaxEthSupply();
    require forall address u. mirrorDeposits[u] <= sumDeposits;
    env e;
    calldataarg args;
    address a;
    uint256 depositBefore = currentContract.deposits[a].deposit;
    bool stakedBefore = currentContract.deposits[a].staked;
    uint112 stakeBefore = currentContract.deposits[a].stake;
    uint32 unstakeDelaySecBefore = currentContract.deposits[a].unstakeDelaySec;
    uint48 withdrawTimeBefore = currentContract.deposits[a].withdrawTime;

    if (f.selector == sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector) {
        env eF;
        bytes b1;
        EntryPoint.UserOpInfo opInfo;
        require opInfo.prefund + sumDeposits + sumStakes <= THEORETICAL_MAX_ETH_SUPPLY();
        bytes b2;
        innerHandleOp(eF, b1, opInfo, b2);
    } else {
        f(e, args);
    }
    
    uint256 depositAfter = currentContract.deposits[a].deposit;
    bool stakedAfter = currentContract.deposits[a].staked;
    uint112 stakeAfter = currentContract.deposits[a].stake;
    uint32 unstakeDelaySecAfter = currentContract.deposits[a].unstakeDelaySec;
    uint48 withdrawTimeAfter = currentContract.deposits[a].withdrawTime;

    assert depositBefore == depositAfter // no change
            || (depositAfter >= depositBefore && f.selector == sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector) // deposit increase by refund
            || (depositAfter >= depositBefore && a == currentContract && f.selector != sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector) // deposit increase by compensation with EntryPoint as beneficiary
            || (depositAfter <= depositBefore && f.selector != sig:innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector) // deposit decrease due to having no paymaster
            ;
    assert stakedBefore == stakedAfter;
    assert stakeBefore == stakeAfter;
    assert unstakeDelaySecBefore == unstakeDelaySecAfter;
    assert withdrawTimeBefore == withdrawTimeAfter;
}
