# Sort Colors: https://leetcode.com/problems/sort-colors/

# O(n) time | O(1) space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:  # red
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:  # white
                white += 1
            else:  # blue
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

# Test cases
nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)  # Expected output: [0,0,1,1,2,2]

nums = [2, 0, 1]
Solution().sortColors(nums)
print(nums)  # Expected output: [0,1,2]