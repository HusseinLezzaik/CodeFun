# Container With Most Water: https://leetcode.com/problems/container-with-most-water/

# O(n) time | O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the maximum water to 0
        max_water = 0

        # Initialize the left and right pointers to the beginning and end of the array
        left, right = 0, len(height) - 1

        # Keep track of the maximum height on the left and right sides
        max_left, max_right = 0, 0

        # Move the left and right pointers towards each other until they meet
        while left < right:
            # Update the maximum height on the left and right sides
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            # If the height on the left is less than the height on the right,
            # move the left pointer towards the right to increase the width
            if height[left] < height[right]:
                water = (right - left) * max_left
                left += 1
            # Otherwise, move the right pointer towards the left to increase the width
            else:
                water = (right - left) * max_right
                right -= 1

            # Update the maximum water
            max_water = max(max_water, water)

        # Return the maximum water
        return max_water

# Test cases
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))  # Expected output: 49

height = [1,1]
print(Solution().maxArea(height))  # Expected output: 1