# Same Tree: https://leetcode.com/problems/same-tree/
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Test the isSameTree function
sol = Solution()

# Create two binary trees for testing
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print("Are the two binary trees the same?", sol.isSameTree(p, q))  # Expected: True