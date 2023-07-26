"""
Lowest Common Ancestor in a Binary Tree:

This problem involves finding the lowest common ancestor (LCA) of two given nodes in the tree. It can be solved using recursion or parent pointers.
"""

# O(N) time | O(N) space
class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            if not current_node:
                return False
            
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            
            mid = current_node == p or current_node == q
            
            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right

        recurse_tree(root)
        return self.ans

# Test the lowestCommonAncestor function
sol = Solution()
lca = sol.lowestCommonAncestor(root, root.left.right, root)  # p = 5, q = 1
print("Lowest Common Ancestor of 5 and 1:", lca.val)  # Expected: 1

sol = Solution()
lca = sol.lowestCommonAncestor(root, root.left.right, root.left.left)  # p = 5, q = 4
print("Lowest Common Ancestor of 5 and 4:", lca.val)  # Expected: 2
