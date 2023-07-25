# Subsets II: https://leetcode.com/problems/subsets-ii/
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

# O(n*2^n) time | O(n) space
def subsetsWithDup(nums):
    def backtrack(start, end, tmp):
        ans.append(tmp[:])
        for i in range(start, end):
            if i > start and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            backtrack(i+1, end, tmp)
            tmp.pop()

    nums.sort()
    ans = []
    backtrack(0, len(nums), [])
    return ans

# Test Cases
print(subsetsWithDup([1,2,2]))  # Expected output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
print(subsetsWithDup([0]))  # Expected output: [[],[0]]