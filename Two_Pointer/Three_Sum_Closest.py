# 3Sum Closest: https://leetcode.com/problems/3sum-closest/

# O(n^2) time | O(1) space
def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
                
    return closest_sum

# Test cases
print(three_sum_closest([-1, 2, 1, -4], 1))  # Expected output: 2
print(three_sum_closest([1, 1, -1, -1, 3], -1))  # Expected output: -1
print(three_sum_closest([1, 2, 4, 8, 16, 32, 64, 128], 82))  # Expected output: 82
print(three_sum_closest([0, 2, 1, -3], 1))  # Expected output: 0
