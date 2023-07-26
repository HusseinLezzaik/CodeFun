# Diameter of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/

# O(N) time | O(h) space - where N is the number of nodes in the binary tree and h is the height of the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, node):
        if not node:
            return 0

        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)

        self.diameter = max(self.diameter, left_depth + right_depth)

        return max(left_depth, right_depth) + 1

# Test the diameterOfBinaryTree function
sol = Solution()

# Create a binary tree for testing
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter of the tree:", sol.diameterOfBinaryTree(root))  # Expected: 3