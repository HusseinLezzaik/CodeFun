# Path Sum: https://leetcode.com/problems/path-sum/
"""
Time complexity: O(N), where N is the number of nodes in the tree. This is because we visit each node exactly once.
Space complexity: O(h), where h is the height of the tree. This is due to the maximum amount of space needed in the call stack for the recursion, which is proportional to the height of the tree. In the worst case scenario (when the tree is a straight line), the height of the tree is N, so the space complexity would be O(N).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# Test the hasPathSum function
sol = Solution()

# Create a binary tree for testing
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

targetSum = 22
print("Does the tree have a root-to-leaf path summing up to the target?", sol.hasPathSum(root, targetSum))  # Expected: True