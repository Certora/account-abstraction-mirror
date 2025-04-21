definition alwaysReverting(method f) returns bool = 
    f.selector == sig:getSenderAddress(bytes).selector 
    || f.selector == sig:delegateAndRevert(address,bytes).selector;

//// # Verifies that certain function always revert as expected */
rule alwaysRevert(method f)
filtered { f -> alwaysReverting(f) }
{
    env e;
    calldataarg args;
    f@withrevert(e,args);
    assert lastReverted;
}