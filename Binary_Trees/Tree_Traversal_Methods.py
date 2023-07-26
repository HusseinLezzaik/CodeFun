"""
There are mainly three types of depth-first traversal:

In-order traversal: In this traversal method, the left subtree is visited first, then the root and later the right subtree.
Pre-order traversal: In this traversal method, the root node is visited first, then the left subtree and finally the right subtree.
Post-order traversal: In this traversal method, the root node is visited last, so the order is left subtree, right subtree, and finally the root node.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Helper function for tree traversal
def traverse(root, order):
    if root is None:
        return []
    
    if order == "in":
        return traverse(root.left, order) + [root.val] + traverse(root.right, order)
    elif order == "pre":
        return [root.val] + traverse(root.left, order) + traverse(root.right, order)
    elif order == "post":
        return traverse(root.left, order) + traverse(root.right, order) + [root.val]
    else:
        return []

# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test the tree traversal methods
print("In-order traversal:", traverse(root, "in"))  # Expected: [4, 2, 5, 1, 3]
print("Pre-order traversal:", traverse(root, "pre"))  # Expected: [1, 2, 4, 5, 3]
print("Post-order traversal:", traverse(root, "post"))  # Expected: [4, 5, 2, 3, 1]
