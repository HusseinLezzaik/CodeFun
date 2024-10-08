"""
First Missing Positive:
Given an unsorted integer array, find the smallest missing positive integer.
"""

def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Modify the array to ignore non-positive and too large numbers
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # Step 2: Mark existing numbers
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])
    
    # Step 3: Find the first missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1
    
    # If we didn't find a missing number, the answer is n + 1
    return n + 1

# Test cases
test_cases = [
    [1, 2, 0],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12],
    [1]
]

for case in test_cases:
    print(f"Input: {case}")
    result = firstMissingPositive(case)
    print(f"First missing positive: {result}\n")