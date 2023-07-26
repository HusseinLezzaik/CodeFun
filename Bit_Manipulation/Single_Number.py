# Single Number: https://leetcode.com/problems/single-number/

"""
The properties of the XOR operation that we'll use are:
1) XOR of a number with itself is 0.
2) XOR of a number with 0 is the number itsel
"""
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test cases
print(single_number([2, 2, 1]))  # Expected: 1
print(single_number([4, 1, 2, 1, 2]))  # Expected: 4
print(single_number([1]))  # Expected: 1
print(single_number([2, 2, 3, 3, 4, 4, 1, 1, 5]))  # Expected: 5
print(single_number([-1, -1, -2]))  # Expected: -2