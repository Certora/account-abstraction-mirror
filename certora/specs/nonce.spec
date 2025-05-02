import "./management.spec";

methods {
    // mark getNonce as envfree
    function getNonce(address,uint192) external returns uint256 envfree;

    // optimization here, checking it does not touch the nonce 
    function NonceHarness.innerHandleOp(
        bytes, 
        EntryPoint.UserOpInfo, 
        bytes
    ) external returns uint256 => NONDET;
    function EntryPoint._executeUserOp(
        uint256 opIndex,
        EntryPoint.PackedUserOperation calldata userOp,
        EntryPoint.UserOpInfo memory opInfo
    ) internal returns (uint256) => NONDET;
    function EntryPoint._validateAccountAndPaymasterValidationData(
        uint256 opIndex,
        uint256 validationData,
        uint256 paymasterValidationData,
        address expectedAggregator
    ) internal => NONDET; // view function, no need to check if it updates nonce
}

function nonceKey(uint256 nonce) returns uint192 {
    return assert_uint192(nonce >> 64);
}

// the nonce consists of 192 bytes of key, followed by 64 bytes of sequence
// question: why the sequence number is 256 bits and not 64?

//// # Validate and update nonce returns true on current nonce only
rule nonceValidation() {
    env e;
    address sender;
    uint192 key;
    requireInvariant nonceSequenceBound(sender, key);
    require currentContract.nonceSequenceNumber[sender][key] > 0; // incremented at least once
    uint256 maybeNonce;
    require nonceKey(maybeNonce) == key;
    // for a certain sender and key, validateAndUpdateNonce is only successful on the current sequence number
    assert maybeNonce == getNonce(sender, key) <=> validateAndUpdateNonce(e, sender, maybeNonce);
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

//// # Nonce sequence must be bound by 2^64 (taking a grace of 1 unit)
invariant nonceSequenceBound(address sender, uint192 key)
    currentContract.nonceSequenceNumber[sender][key] < max_uint64
filtered { f -> !alwaysReverting(f) } {
    preserved with (env e) {
        // strengthen the invariant since when we increment it can go from max_uint64 to 2**64 and 
        // for ease of use in other rules we prefer it doesn't start at the edge max_uint64 either.
        require currentContract.nonceSequenceNumber[sender][key] < max_uint64 - 1;
    }
}

//// # Inner-handle-op does not change nonce
rule innerHandleOpDoesNotChangeNonce()
{
    address sender;
    uint192 key;

    env e;
    calldataarg args;
    
    uint256 nonceBefore = getNonce(sender, key);
    
    innerHandleOp(e, args);
    
    uint256 nonceAfter = getNonce(sender, key);
    assert nonceAfter == nonceBefore;
}

//// # execute-user-op does not change nonce
rule executeUserOpDoesNotChangeNonce() 
{
    address sender;
    uint192 key;

    env e;
    calldataarg args;
    
    uint256 nonceBefore = getNonce(sender, key);
    
    executeUserOp(e, args);
    
    uint256 nonceAfter = getNonce(sender, key);
    assert nonceAfter == nonceBefore;
}