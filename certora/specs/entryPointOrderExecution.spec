import "./alwaysRevert.spec";

methods {
    unresolved external in _._ => DISPATCH [
        EntryPoint.innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes),
    ] default ASSERT_FALSE;

    function _executeUserOp(
        uint256 opIndex,
        EntryPoint.PackedUserOperation calldata userOp,
        EntryPoint.UserOpInfo memory opInfo
    ) internal returns (uint256) => executeUserOpHashing(userOp);


    

    // abstract everything else
    function _.validateUserOp(
        EntryPoint.PackedUserOperation userOp,
        bytes32 hash,
        uint256 missingFunds
    ) external => NONDET;
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
ghost mathint seenHashes;

function executeUserOpHashing(EntryPoint.PackedUserOperation userOp) returns uint256 {
    if (seenHashes == 0) {
        assert userOpHash1 == keccak256(userOp.callData);
    }
    if (seenHashes == 1) {
        assert userOpHash2 == keccak256(userOp.callData);
    }
    if (seenHashes == 2) {
        assert userOpHash3 == keccak256(userOp.callData);
    }
    seenHashes = seenHashes + 1;

    uint256 nondet;
    return nondet;
}

rule iterationOrder_HandleOps {
    env e;
    EntryPoint.PackedUserOperation[] ops;
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