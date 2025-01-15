import "./entryPointShared.spec";

persistent ghost mathint prevNumExecuted;

persistent ghost bool inputCalldataLengthIsZero;

hook REVERT(uint offset, uint size) {
    assert numExecuted == prevNumExecuted + 1 || inputCalldataLengthIsZero;
}

function cvlInnerHandleOp(env e) returns uint256 {
    // not supposed to be summarized in residual
    assert false;
	uint toRet;
	return toRet;
}

rule checkInnerHandleOp() {
    prevNumExecuted = numExecuted;

    env e;
    bytes callData;
    inputCalldataLengthIsZero = callData.length == 0;
    EntryPoint.UserOpInfo opInfo;
    bytes context;
    minimalGas = opInfo.mUserOp.callGasLimit + opInfo.mUserOp.paymasterPostOpGasLimit + 10000 /* Inner gas overhead */;

    require e.msg.value == 0;
    require e.msg.sender == entryPoint;

    innerHandleOp@withrevert(e, callData, opInfo, context);
    bool reverted = lastReverted;
    // it is okay if innerHandleOp reverted (unless it's a natural out-of-gas, which we do not reason about but shouldn't happen)
    // but if it succeeded, it must be the case that either:
    // (1) we executed successfully
    // (2) we got nothing to execute (callData length is 0) which should be checked at call site
    assert reverted || numExecuted == prevNumExecuted + 1 || inputCalldataLengthIsZero;
    // use independent satisfies
    satisfy reverted;
    satisfy numExecuted == prevNumExecuted + 1;
    satisfy inputCalldataLengthIsZero;
}