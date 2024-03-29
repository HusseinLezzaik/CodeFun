# Largest Rectangle Area in a Histogram: https://leetcode.com/problems/largest-rectangle-in-histogram/

# Time Complexity: O(n) | Space Complexity: O(n)
def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))  # Outputs: 10

heights = [2,4]
print(largestRectangleArea(heights))  # Outputs: 4