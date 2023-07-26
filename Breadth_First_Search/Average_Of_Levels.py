# Average of Levels in Binary Tree: https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque

# O(N) time | O(M) space - where N is the number of nodes in the tree and M is the maximum number of nodes at any level in the binary tree. 
class Solution:
    def averageOfLevels(self, root):
        if not root:
            return []
        
        result, queue = [], deque([(root, 0)])
        
        while queue:
            node, level = queue.popleft()
            if level == len(result):
                result.append([node.val, 1])
            else:
                result[level][0] += node.val
                result[level][1] += 1
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return [s / float(c) for s, c in result]

# Test the averageOfLevels function
sol = Solution()
print("Average of nodes at each level:", sol.averageOfLevels(root))  # Expected: [1.0, 2.5, 4.5]
