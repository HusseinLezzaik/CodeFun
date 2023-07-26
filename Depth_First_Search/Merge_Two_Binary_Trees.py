# Merge Two Binary Trees: https://leetcode.com/problems/merge-two-binary-trees/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time | O(h) space - where N is the number of nodes in the binary tree and h is the height of the binary tree
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

# Test the mergeTrees function
sol = Solution()

# Create two binary trees for testing
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

merged_tree = sol.mergeTrees(root1, root2)

# Function to print tree nodes in pre-order traversal
def print_tree(root):
    if not root:
        return
    print(root.val, end=' ')
    print_tree(root.left)
    print_tree(root.right)

print("Merged tree in pre-order traversal:", end=' ')
print_tree(merged_tree)  # Expected: 3 4 5 4 5 7