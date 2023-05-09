class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
            n = len(nums)
            for i in range(n):
                while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
            # Iterate through the sorted array to find the first missing positive number
            for i in range(n):
                if nums[i] != i + 1:
                    return i + 1
                    
            # If all positive integers are in the array, return the next integer (n+1)
            return n + 1
