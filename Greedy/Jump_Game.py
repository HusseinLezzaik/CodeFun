# Jump Game: https://leetcode.com/problems/jump-game/

# O(N) time, O(1) space
def canJump(nums):
    lastPos = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastPos:
            lastPos = i
    return lastPos == 0

# Test Cases
print(canJump([2, 3, 1, 1, 4]))  # Expected output: True
print(canJump([3, 2, 1, 0, 4]))  # Expected output: False
print(canJump([0]))  # Expected output: True