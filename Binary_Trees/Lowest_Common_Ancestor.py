"""
Lowest Common Ancestor in a Binary Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

This problem involves finding the lowest common ancestor (LCA) of two given nodes in the tree. It can be solved using recursion or parent pointers.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) time | O(n) space
def lowestCommonAncestor(root, p, q):
    ans = None

    def recurse_tree(current_node):
        nonlocal ans
        if not current_node:
            return False

        left = recurse_tree(current_node.left)
        right = recurse_tree(current_node.right)

        mid = current_node == p or current_node == q

        if mid + left + right >= 2:
            ans = current_node

        return mid or left or right

    recurse_tree(root)
    return ans

# Let's construct a binary tree and test the function
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

# In this tree, the lowest common ancestor of nodes with values 5 and 1 is the root node with value 3.
node1 = root.left  # Node with value 5
node2 = root.right  # Node with value 1
lca = lowestCommonAncestor(root, node1, node2)
print(lca.val if lca else None)  # Expect: 3

# In this tree, the lowest common ancestor of nodes with values 6 and 2 is the node with value 5.
node1 = root.left.left  # Node with value 6
node2 = root.left.right  # Node with value 2
lca = lowestCommonAncestor(root, node1, node2)
print(lca.val if lca else None)  # Expect: 5

