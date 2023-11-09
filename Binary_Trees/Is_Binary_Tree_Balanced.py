"""
Check if Binary Tree Is Balanced:

This problem requires checking whether a tree is height-balanced, meaning for each node in the tree,
the height difference between the left and right subtree is no more than 1. It is typically solved using recursion.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
1. if empty, return 0
2. compute the left and right most heights
3. when done, check if the left and right subtrees are balanced - if not return -1
4. if balanced, return the height of the tree
"""

# Recursive Algorithm
def height(node):
    if not node:
        return 0
    left_height, right_height = height(node.left), height(node.right)
    if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1

# O(n) time | O(h) space - where n is the number of nodes in the binary tree and h is the height of the binary tree
def isBalanced(root):
    return height(root) >= 0

# construct a balanced binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
root.right.left.left = TreeNode(4)
root.right.left.right = TreeNode(4)

print(isBalanced(root))  # should return True

# construct an unbalanced binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)

print(isBalanced(root))  # should return False