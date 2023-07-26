# Binary Tree Zigag Level Order Traversal: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque

# O(N) time | O(N) space - where N is the number of nodes in the tree
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        results = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            results.append(list(current_level))
            left_to_right = not left_to_right

        return results

# Test the zigzagLevelOrder function
sol = Solution()
print("Zigzag level order traversal of the binary tree:", sol.zigzagLevelOrder(root))  # Expected: [[1], [3, 2], [4, 5]]