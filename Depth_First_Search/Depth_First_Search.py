# Depth First Search Implementation 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(node):
    if node is None:
        return
    
    print(node.value)  # Process the node
    dfs(node.left)  # Recurse on the left subtree
    dfs(node.right)  # Recurse on the right subtree
