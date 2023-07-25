# Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/

# O(N) time, O(1) space
def findDuplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Test Cases
print(findDuplicate([1, 3, 4, 2, 2]))  # Expected output: 2
print(findDuplicate([3, 1, 3, 4, 2]))  # Expected output: 3