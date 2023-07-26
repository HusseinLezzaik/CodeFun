# Subtree of Another Tree: https://leetcode.com/problems/subtree-of-another-tree/
"""
Time complexity: O(M*N), where M is the number of nodes in the main tree and N is the number of nodes in the sub-tree. In the worst case scenario, we have to compare the sub-tree with every sub-tree in the main tree starting at each node.
Space complexity: O(min(M, N)), where M is the number of nodes in the main tree and N is the number of nodes in the sub-tree. This is because the maximum depth of the recursion is the minimum height of the two trees.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Test the isSubtree function
sol = Solution()

# Create two binary trees for testing
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print("Is the sub tree a sub-tree of the main tree?", sol.isSubtree(root, subRoot))  # Expected: True
