# Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
Time complexity: O(N), where N is the minimum number of nodes from the two given trees. This is because we visit each node from the two trees once and only once.
Space complexity: O(h), where h is the height of the resultant tree. This is due to the maximum amount of space needed in the call stack for the recursion, which is proportional to the height of the resultant tree. In the worst case scenario (when the tree is a straight line), the height of the tree is N, so the space complexity would be O(N).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# Test the maxDepth function
sol = Solution()

# Create a binary tree for testing
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Maximum depth of the tree:", sol.maxDepth(root))  # Expected: 3
