import "./entryPointShared.spec";

methods {
    unresolved external in _._ => DISPATCH [
        EntryPoint.innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes),
    ] default ASSERT_FALSE;

}

function cvlInnerHandleOp(env e) returns uint256 {
	assert e.msg.sender == currentContract;
    assert e.msg.value == 0;
    // we are not asserting callData.length > 0 even though it is required for actual execution.
    // the reason is that requiring it here prohibits some critical performance imporvement.
	numExecuted = numExecuted + 1;
	uint toRet;
	return toRet;
}

// a rule checking cvlInnerHandleOp summary - separate spec file: `residual.spec`


//// # Check that every op that exec-ed on an account has been checked via the validateUserOp function
/**
* Verified by keeping track of opcodes that have been verified and executed opcodes
*/


/* everything but handle*Ops functions*/
rule onlyValidatedCalls_NonHandleOps(method f) 
filtered { f -> !isHandleOps(f) }
{
    // check only entrypoint
    require f.contract == entryPoint;
    // delegateAndRevert should always revert anyway, filter out
    require f.selector != sig:delegateAndRevert(address,bytes).selector;
    // innerHandleOp is... inner!
    require f.selector != sig:EntryPoint.innerHandleOp(bytes,EntryPoint.UserOpInfo,bytes).selector;
    check_onlyValidatedCalls_assert(f, 100, 100, 100, 100);
}

/* all variants of handleOps */
rule onlyValidatedCalls_3HandleOps(method f)
filtered { f->
    f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector 
}
{
  check_onlyValidatedCalls_assert(f, 3, 100, 100, 100);
}

rule onlyValidatedCalls_2HandleOps(method f)
filtered { f->
    f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector 
}
{
  check_onlyValidatedCalls_assert(f, 2, 100, 100, 100);
}

rule onlyValidatedCalls_1HandleOps(method f)
filtered { f->
    f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector 
}
{
  check_onlyValidatedCalls_assert(f, 1, 100, 100, 100);
}

rule onlyValidatedCalls_0HandleOps(method f)
filtered { f->
    f.selector == sig:handleOps(EntryPoint.PackedUserOperation[],address).selector 
}
{
  check_onlyValidatedCalls_assert(f, 0, 100, 100, 100);
}

/* all variants of handleAggregatedOps */

// 3 - (0,1,2,3) x (0,1,2,3) x (0,1,2,3)
rule onlyValidatedCalls_3HandleAggregatedOps000(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 0, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps001(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 0, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps002(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 0, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps003(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 0, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps010(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 1, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps011(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 1, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps012(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 1, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps013(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 1, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps020(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 2, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps021(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 2, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps022(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 2, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps023(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 2, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps030(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 3, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps031(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 3, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps032(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 3, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps033(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 0, 3, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps100(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 0, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps101(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 0, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps102(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 0, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps103(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 0, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps110(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 1, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps111(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 1, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps112(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 1, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps113(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 1, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps120(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 2, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps121(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 2, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps122(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 2, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps123(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 2, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps130(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 3, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps131(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 3, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps132(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 3, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps133(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 1, 3, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps200(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 0, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps201(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 0, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps202(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 0, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps203(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 0, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps210(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 1, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps211(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 1, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps212(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 1, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps213(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 1, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps220(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 2, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps221(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 2, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps222(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 2, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps223(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 2, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps230(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 3, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps231(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 3, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps232(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 3, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps233(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 2, 3, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps300(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 0, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps301(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 0, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps302(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 0, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps303(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 0, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps310(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 1, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps311(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 1, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps312(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 1, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps313(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 1, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps320(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 2, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps321(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 2, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps322(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 2, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps323(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 2, 3); }

rule onlyValidatedCalls_3HandleAggregatedOps330(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 3, 0); }

rule onlyValidatedCalls_3HandleAggregatedOps331(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 3, 1); }

rule onlyValidatedCalls_3HandleAggregatedOps332(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 3, 2); }

rule onlyValidatedCalls_3HandleAggregatedOps333(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 3, 3, 3, 3); }


// 2 - (0,1,2,3) x (0,1,2,3)
rule onlyValidatedCalls_2HandleAggregatedOps00(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 0, 0, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps01(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 0, 1, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps02(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 0, 2, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps03(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 0, 3, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps10(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 1, 0, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps11(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 1, 1, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps12(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 1, 2, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps13(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 1, 3, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps20(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 2, 0, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps21(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 2, 1, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps22(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 2, 2, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps23(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 2, 3, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps30(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 3, 0, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps31(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 3, 1, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps32(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 3, 2, 100); }

rule onlyValidatedCalls_2HandleAggregatedOps33(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 2, 3, 3, 100); }


// 1 - 0,1,2,3
rule onlyValidatedCalls_1HandleAggregatedOps0(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 1, 0, 100, 100); }

rule onlyValidatedCalls_1HandleAggregatedOps1(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 1, 1, 100, 100); }

rule onlyValidatedCalls_1HandleAggregatedOps2(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 1, 2, 100, 100); }

rule onlyValidatedCalls_1HandleAggregatedOps3(method f)
filtered { f-> f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector }
{ check_onlyValidatedCalls_assert(f, 1, 3, 100, 100); }

rule onlyValidatedCalls_0HandleAggregatedOps(method f)
filtered { f->
    f.selector == sig:handleAggregatedOps(IEntryPoint.UserOpsPerAggregator[],address).selector
}
{
  check_onlyValidatedCalls_assert(f, 0, 100, 100, 100);
}

function check_onlyValidatedCalls_assert(method f, uint sz, uint subsz0, uint subsz1, uint subsz2) {
    env e;
    calldataarg args;
    numValidated = 0;
    numExecuted = 0;
    executionValidated = true;

    dispatchHandleOps(f, e, sz, subsz0, subsz1, subsz2);
    
    assert numValidated == numExecuted;
    assert executionValidated;
}

