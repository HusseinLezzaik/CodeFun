# Binary Tree Level Order Traversal: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

def levelOrder(root):
    if not root:
        return []
    queue, res = deque([root]), []
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    
    return res

# Let's test our function with a binary tree
# The tree looks like this:
#     3
#    / \
#   9  20
#     /  \
#    15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))  # should print [[3], [9, 20], [15, 7]]