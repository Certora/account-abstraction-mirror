methods {
    // make sure we can only call getNonce from spec
    function getNonce(address,uint192) internal returns uint256 => impossible();
}

function impossible() returns uint256 {
    assert false;
    // unreachable, cvl fluke
    uint i;
    return i;
}

use builtin rule sanity;