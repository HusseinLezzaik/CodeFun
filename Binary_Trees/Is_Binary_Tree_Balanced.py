"""
Check if Binary Tree Is Balanced:

This problem requires checking whether a tree is height-balanced, meaning for each node in the tree,
the height difference between the left and right subtree is no more than 1. It is typically solved using recursion.
"""

# O(N) time | O(H) space
class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            left_height, right_height = height(node.left), height(node.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return height(root) >= 0

# Test the isBalanced function
sol = Solution()
print("Is the binary tree balanced?", sol.isBalanced(root))  # Expected: True