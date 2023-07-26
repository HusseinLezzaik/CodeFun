# Minimum Depth of Binary Tree: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
Time complexity: O(N), where N is the number of nodes in the binary tree. This is because we visit each node exactly once.
Space complexity: O(M), where M is the maximum number of nodes at any level in the binary tree.
This is due to the space needed to store the nodes in the queue for BFS traversal.
"""


from collections import deque

# O(N) time | O(M) space 
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

# Test the minDepth function
sol = Solution()
print("Minimum depth of the binary tree:", sol.minDepth(root))  # Expected: 2
