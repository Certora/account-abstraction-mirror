import "../../contracts/core/EntryPoint.sol";

contract NonceHarness is EntryPoint {
    function validateAndUpdateNonce(address sender, uint256 nonce) external returns (bool) {
        return _validateAndUpdateNonce(sender, nonce);
    }
}