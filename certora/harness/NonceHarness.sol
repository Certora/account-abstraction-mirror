import "../../contracts/core/EntryPoint.sol";

contract NonceHarness is EntryPoint {
    function validateAndUpdateNonce(address sender, uint256 nonce) external returns (bool) {
        return _validateAndUpdateNonce(sender, nonce);
    }

    function executeUserOp(
        uint256 opIndex,
        PackedUserOperation calldata userOp,
        UserOpInfo memory opInfo
    ) external returns (uint256) {
        return _executeUserOp(opIndex, userOp, opInfo); 
    }

    function testBalloon() external {
        getNonce(msg.sender, 0);
    }
}