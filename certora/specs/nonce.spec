import "./management.spec";

methods {
    function getNonce(address,uint192) external returns uint256 envfree;
}

// the nonce consists of 192 bytes of key, followed by 64 bytes of sequence

// question: why the sequence number is 256 bits and not 64?

//// # Validate and update nonce returns true on current nonce
rule nonceValidation() {
    env e;
    address sender;
    uint192 key;
    requireInvariant nonceSequenceBound(sender, key);
    require currentContract.nonceSequenceNumber[sender][key] > 0; // incremented at least once
    assert validateAndUpdateNonce(e, sender, require_uint256(getNonce(sender, key)));
}

//// # Nonce is monotone increasing
rule nonceMonotoneIncreasing(method f) 
filtered { f -> !alwaysReverting(f) }
{
    address sender;
    uint192 key;

    requireInvariant nonceSequenceBound(sender, key);

    uint256 nonceBefore = getNonce(sender, key);

    env e;
    calldataarg args;
    f(e, args);

    uint256 nonceAfter = getNonce(sender, key);
    assert nonceAfter == nonceBefore || nonceAfter == nonceBefore + 1;
}

//// # Nonce sequence must be bound by 2^64
invariant nonceSequenceBound(address sender, uint192 key)
    currentContract.nonceSequenceNumber[sender][key] <= max_uint64
filtered { f -> !alwaysReverting(f) }