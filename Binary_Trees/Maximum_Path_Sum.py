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
# First, let's remove the class method format and convert the function to a normal Python function

def maxPathSum(root):
    max_sum = float('-inf')

    def _maxPathSum(node):
        nonlocal max_sum
        if not node:
            return 0

        left_gain = max(_maxPathSum(node.left), 0)
        right_gain = max(_maxPathSum(node.right), 0)
        
        price_newpath = node.val + left_gain + right_gain

        max_sum = max(max_sum, price_newpath)

        return node.val + max(left_gain, right_gain)

    _maxPathSum(root)
    return max_sum

# Now let's construct a binary tree and test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# For this tree, the maximum path sum is 6 (2 -> 1 -> 3)
print(maxPathSum(root))  # Expect: 6

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# For this tree, the maximum path sum is 42 (15 -> 20 -> 7)
print(maxPathSum(root))  # Expect: 42

