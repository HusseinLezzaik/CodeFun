# Missing Number: https://leetcode.com/problems/missing-number/

# O(n) time | O(1) space
def missing_number(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

# Test cases
print(missing_number([3, 0, 1]))  # Expected: 2
print(missing_number([0, 1]))  # Expected: 2
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # Expected: 8
print(missing_number([0]))  # Expected: 1
print(missing_number([1]))  # Expected: 0