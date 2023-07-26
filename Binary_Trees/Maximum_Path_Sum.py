"""
Binary Tree Maximum Path Sum: This problem requires finding a path in the tree such that the sum of the nodes on the path is maximized. 
It is typically solved using recursion.

The time complexity of the maxPathSum function is O(N), where N is the number of nodes in the binary tree.
This is because we visit each node exactly once during the post-order traversal.

The space complexity of the function is O(H), where H is the height of the binary tree. 
This space is used by the call stack for the recursive calls. In the worst case, if the binary tree is skewed, 
the height of the tree is N, so the space complexity could also be considered O(N) in the worst-case scenario.
However, for a balanced binary tree, the height of the tree is log(N), so the space complexity is O(log(N)).
"""

# O(N) time | O(logN) space - where N is the number of nodes in the binary tree
class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        self._maxPathSum(root)
        return self.max_sum

    def _maxPathSum(self, node):
        if not node:
            return 0

        left_gain = max(self._maxPathSum(node.left), 0)
        right_gain = max(self._maxPathSum(node.right), 0)
        
        price_newpath = node.val + left_gain + right_gain

        self.max_sum = max(self.max_sum, price_newpath)

        return node.val + max(left_gain, right_gain)
    
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test the maxPathSum function
sol = Solution()
print("Maximum path sum:", sol.maxPathSum(root))  # Expected: 15
