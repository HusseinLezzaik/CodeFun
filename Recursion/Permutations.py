# Permutations: https://leetcode.com/problems/permutations/

"""
The time complexity is O(NxN!) because there are N! possible permutations for a list of length N, and we spend O(N) time to store a copy of each.
The space complexity is O(NxN!) to store all the permutations.
"""

def permute(nums):
    def backtrack(first = 0):
        # if all integers are used up
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first 
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
 
    n = len(nums)
    output = []
    backtrack()
    return output

