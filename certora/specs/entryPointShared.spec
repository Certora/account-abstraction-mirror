using EntryPoint as entryPoint;

methods {

    function Exec.call(
        address to,
        uint256 value,
        bytes memory data,
        uint256 txGas
    ) internal returns (bool) => execCallSummary(to, value, data, txGas);
    
    function _.createSender(bytes initCode) external => NONDET;

    function _.validateUserOp(
        EntryPoint.PackedUserOperation userOp,
        bytes32 hash,
        uint256 missingFunds
    ) external => validateUserOpSummary() expect uint256;
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


    function balanceOf(address) external returns (uint256) envfree;
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

    function calldataKeccak(bytes calldata data) internal returns bytes32 => keccak256(data);

    function EntryPoint.innerHandleOp(
        bytes, 
        EntryPoint.UserOpInfo, 
        bytes
    ) external returns uint256 with (env e) => cvlInnerHandleOp(e);

    

    // optimizations
    function emitUserOperationEvent(EntryPoint.UserOpInfo memory opInfo, bool success, uint256 actualGasCost, uint256 actualGas) internal => NONDET;
    function emitPrefundTooLow(EntryPoint.UserOpInfo memory opInfo) internal => NONDET;
    function Exec.getReturnData(uint256) internal returns (bytes memory) => nondetBytes();

}

persistent ghost mathint numValidated;
persistent ghost mathint numExecuted;
persistent ghost bool executionValidated;

function nondetBytes() returns bytes {
    bytes b;
    return b;
}

function validateUserOpSummary() returns uint256 {
    numValidated = numValidated + 1;
    uint256 validationData;
    return validationData;
}

function execCallSummary(address to, uint256 value, bytes data, uint256 txGas) returns bool {
    if (numExecuted >= numValidated) {
        executionValidated = false;
    }
    numExecuted = numExecuted + 1;
    bool result;
    return result;
}


function limitPerAggregatorOps(IEntryPoint.UserOpsPerAggregator[] op, uint idx, uint subsz) {
    require op[idx].userOps.length == subsz;
}

function dispatchHandleOps(method f, env e, uint sz, uint subsz0, uint subsz1, uint subsz2) {
    if (f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector) {
        EntryPoint.PackedUserOperation[] ops;
        assert sz <= 3, "We prove up to size 3"; 
        require ops.length == sz;
        address beneficiary;
        handleOps(e,ops,beneficiary);
    } else if (f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector) {
        IEntryPoint.UserOpsPerAggregator[] ops;
        assert sz <= 3, "We prove up to size 3"; 
        require ops.length == sz;
        if (ops.length >= 1) {
            limitPerAggregatorOps(ops, 0, subsz0);
            if (ops.length >= 2) {
                limitPerAggregatorOps(ops, 1, subsz1);
                if (ops.length >= 3) {
                    limitPerAggregatorOps(ops, 2, subsz2);
                }
            }
        }
        address beneficiary;
        handleAggregatedOps(e,ops,beneficiary);
    } else {
        // xx add handle aggregated ops
        calldataarg args;
        f(e, args);
    }
}

definition isHandleOps(method f) returns bool = 
    f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector 
    || f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector;
