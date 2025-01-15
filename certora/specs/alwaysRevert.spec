
//// # Verifies that certain function always revert as expected */
rule alwaysRevert(method f)
filtered { f->
    f.selector == sig:getSenderAddress(bytes).selector 
    || f.selector == sig:delegateAndRevert(address,bytes).selector
}
{
    env e;
    calldataarg args;
    f@withrevert(e,args);
    assert lastReverted;
}