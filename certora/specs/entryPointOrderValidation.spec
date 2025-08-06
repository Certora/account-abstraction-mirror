import "./alwaysRevert.spec";

methods {
    unresolved external in _._ => DISPATCH [
        EntryPoint.innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes),
    ] default ASSERT_FALSE;

    function _.validateUserOp(
        EntryPoint.PackedUserOperation userOp,
        bytes32 hash,
        uint256 missingFunds
    ) external => validateUserOpSummaryHashing(userOp) expect uint256;


    // abstract everything else

    function Exec.call(
        address to,
        uint256 value,
        bytes memory data,
        uint256 txGas
    ) internal returns (bool) => NONDET;
    function _.createSender(bytes initCode) external => NONDET;
    function _.validatePaymasterUserOp(
        EntryPoint.PackedUserOperation userOp, 
        bytes32 userOpHash, 
        uint256 maxCost
    ) external => NONDET;
    function _.validateSignatures(
        EntryPoint.PackedUserOperation[] userOps,
        bytes signature
    ) external => NONDET;
    function EntryPoint.getUserOpHash(EntryPoint.PackedUserOperation calldata) internal returns bytes32 => NONDET;
    function _callValidatePaymasterUserOp(
        uint256 opIndex,
        EntryPoint.PackedUserOperation calldata op,
        EntryPoint.UserOpInfo memory opInfo) internal returns (bytes memory, uint256) => cvlCallValidatePaymasterUserOp();

    function _compensate(address beneficiary, uint256 amount) internal  => NONDET;
    function _createSenderIfNeeded(
        uint256 opIndex, 
        EntryPoint.UserOpInfo memory opInfo, 
        bytes calldata initCode
    ) internal => NONDET;

    function _.postOp(
        IPaymaster.PostOpMode mode, 
        bytes context, 
        uint256 actualGasCost, 
        uint256 actualUserOpFeePerGas
    ) external => NONDET;

    function EntryPoint.innerHandleOp(
        bytes, 
        EntryPoint.UserOpInfo, 
        bytes
    ) external returns uint256 => NONDET;

    function StakeManager._tryDecrementDeposit(address account, uint256 amount) internal returns(bool) => NONDET;
    function _validateAccountAndPaymasterValidationData(
        uint256 opIndex,
        uint256 validationData,
        uint256 paymasterValidationData,
        address expectedAggregator
    ) internal => NONDET;
    function _executeUserOp(
        uint256 opIndex,
        EntryPoint.PackedUserOperation calldata userOp,
        EntryPoint.UserOpInfo memory opInfo
    ) internal returns (uint256) => NONDET;

    // optimizations
    function _.calldataKeccak(bytes calldata data) internal => keccak256(data) expect bytes32;
    function _emitUserOperationEvent(EntryPoint.UserOpInfo memory opInfo, bool success, uint256 actualGasCost, uint256 actualGas) internal => NONDET;
    function _emitPrefundTooLow(EntryPoint.UserOpInfo memory opInfo) internal => NONDET;
    function Exec.getReturnData(uint256) internal returns (bytes memory) => nondetBytes();

}

function nondetBytes() returns bytes {
    bytes b;
    return b;
}

function cvlCallValidatePaymasterUserOp() returns (bytes, uint256) {
    bytes context;
    uint256 validationData;
    return (context, validationData);
}

ghost bytes32 userOpHash1;
ghost bytes32 userOpHash2;
ghost bytes32 userOpHash3;
// ghost bytes32 userOpHash4;
// ghost bytes32 userOpHash5;
// ghost bytes32 userOpHash6;
ghost mathint seenHashes;

function validateUserOpSummaryHashing(EntryPoint.PackedUserOperation userOp) returns uint256 {
    if (seenHashes == 0) {
        assert userOpHash1 == keccak256(userOp.callData);
    }
    if (seenHashes == 1) {
        assert userOpHash2 == keccak256(userOp.callData);
    }
    if (seenHashes == 2) {
        assert userOpHash3 == keccak256(userOp.callData);
    }
    // if (seenHashes == 3) {
    //     assert userOpHash4 == keccak256(userOp.callData);
    // }
    // if (seenHashes == 4) {
    //     assert userOpHash5 == keccak256(userOp.callData);
    // }
    // if (seenHashes == 5) {
    //     assert userOpHash6 == keccak256(userOp.callData);
    // }
    seenHashes = seenHashes + 1;

    uint256 nondet;
    return nondet;
}

rule iterationOrder_HandleOps {
    env e;
    IEntryPoint.PackedUserOperation[] ops;
    require ops.length <= 3;
    if (ops.length >= 1) {
        userOpHash1 = keccak256(ops[0].callData);
    }
    if (ops.length >= 2) {
        userOpHash2 = keccak256(ops[1].callData);
    }
    if (ops.length >= 3) {
        userOpHash3 = keccak256(ops[2].callData);
    }
    seenHashes = 0;
    address beneficiary;
    handleOps(e,ops,beneficiary);
    assert true;
}
/*
rule iterationOrder_HandleAggregatedOps {
    env e;
    calldataarg args;
    seenHashes = 0;
    IEntryPoint.UserOpsPerAggregator[] ops;
    require ops.length == 2;
    require ops[0].userOps.length == 1;
    require ops[1].userOps.length == 1;
    // require ops[2].userOps.length == 1;
    userOpHash1 = keccak256(ops[0].userOps[0].callData);
    // userOpHash2 = keccak256(ops[0].userOps[1].callData);
    userOpHash2 = keccak256(ops[1].userOps[0].callData);
    // userOpHash4 = keccak256(ops[1].userOps[1].callData);
    // userOpHash5 = keccak256(ops[2].userOps[0].callData);
    // userOpHash6 = keccak256(ops[2].userOps[1].callData);
    address beneficiary;
    handleAggregatedOps(e,ops,beneficiary);
    assert true;
}
*/
/** Too expensive? */
/*
rule iterationOrder_HandleAggregatedOps {
    env e;
    IEntryPoint.UserOpsPerAggregator[] ops;
    require ops.length == 2;
    userOpHash1 = ops.length >= 1 && ops[0].userOps.length >= 1 ? keccak256(ops[0].userOps[0].callData)
                 : ops.length >= 2 && ops[1].userOps.length >= 1 ? keccak256(ops[1].userOps[0].callData)
                 : ops.length >= 3 && ops[2].userOps.length >= 1 ? keccak256(ops[2].userOps[0].callData)
                 : to_bytes32(0);
    userOpHash2 = ops.length >= 1 && ops[0].userOps.length >= 2 ? keccak256(ops[0].userOps[1].callData)
                 : ops.length >= 2 && ops[1].userOps.length >= 2 ? keccak256(ops[1].userOps[1].callData)
                 : ops.length >= 3 && ops[2].userOps.length >= 2 ? keccak256(ops[2].userOps[1].callData)
                 : to_bytes32(0);
    userOpHash3 = ops.length >= 1 && ops[0].userOps.length >= 3 ? keccak256(ops[0].userOps[2].callData)
                 : ops.length >= 2 && ops[1].userOps.length >= 3 ? keccak256(ops[1].userOps[2].callData)
                 : ops.length >= 3 && ops[2].userOps.length >= 3 ? keccak256(ops[2].userOps[2].callData)
                 : to_bytes32(0);
    userOpHash4 = ops.length >= 2 && ops[0].userOps.length == 3 && ops[1].userOps.length >= 1 ? keccak256(ops[1].userOps[0].callData)
                 : ops.length >= 2 && ops[0].userOps.length == 2 && ops[1].userOps.length >= 2 ? keccak256(ops[1].userOps[1].callData)
                 : ops.length >= 2 && ops[0].userOps.length == 1 && ops[1].userOps.length >= 3 ? keccak256(ops[1].userOps[2].callData)
                 : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 3 && ops[2].userOps.length >= 1? keccak256(ops[2].userOps[0].callData)
                 : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 2 && ops[2].userOps.length >= 2 ? keccak256(ops[2].userOps[1].callData)
                 : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 1 && ops[2].userOps.length >= 3 ? keccak256(ops[2].userOps[2].callData)
                 : to_bytes32(0);

    userOpHash5 = ops.length >= 2 && ops[0].userOps.length == 3 && ops[1].userOps.length >= 2 ? keccak256(ops[1].userOps[1].callData)
                : ops.length >= 2 && ops[0].userOps.length == 2 && ops[1].userOps.length >= 3 ? keccak256(ops[1].userOps[2].callData)
                : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 4 && ops[2].userOps.length >= 1 ? keccak256(ops[2].userOps[0].callData)
                : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 3 && ops[2].userOps.length >= 2 ? keccak256(ops[2].userOps[1].callData) 
                : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 2 && ops[2].userOps.length >= 3 ? keccak256(ops[2].userOps[2].callData)
                : to_bytes32(0);

    userOpHash6 = ops.length >= 2 && ops[0].userOps.length+ops[1].userOps.length == 6 ? keccak256(ops[1].userOps[2].callData)
                : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 5 && ops[2].userOps.length >= 1 ? keccak256(ops[2].userOps[0].callData)
                : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 4 && ops[2].userOps.length >= 2 ? keccak256(ops[2].userOps[1].callData)
                : ops.length >= 3 && ops[0].userOps.length+ops[1].userOps.length <= 3 && ops[2].userOps.length >= 3 ? keccak256(ops[2].userOps[2].callData)
                : to_bytes32(0);
    seenHashes = 0;
    address beneficiary;
    handleAggregatedOps(e,ops,beneficiary);
    assert true;  
}
*/