# Depth First Search Implementation 
"""
many problems in binary trees often require a depth first search traversal of the tree.
it's pretty easy and straight-forward to use, just keep in mind that we're going deep instead of level by level.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# O(n) time - O(h) space - where n is the number of nodes in the tree and h is the height of the tree
def dfs(node):
    if node is None:
        return
    
    print(node.value)  # Process the node
    dfs(node.left)  # Recurse on the left subtree
    dfs(node.right)  # Recurse on the right subtree
