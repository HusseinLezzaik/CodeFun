# All Nodes Distance K in Binary Tree: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time | O(N) space - where N is the number of nodes in the tree
class Solution:
    def distanceK(self, root, target, K):
        graph = defaultdict(list)

        def build_graph(node, parent=None):
            if node:
                if parent:
                    graph[parent.val].append(node.val)
                    graph[node.val].append(parent.val)
                build_graph(node.left, node)
                build_graph(node.right, node)

        build_graph(root)
        queue = deque([(target.val, 0)])
        seen = {target.val}

        while queue:
            node, depth = queue.popleft()
            if depth == K:
                return [node] + [n for n, d in queue if d == K]
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return []

# Create a binary tree for testing
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.right = TreeNode(0)

# Test the distanceK function
sol = Solution()
target = root.left  # Node with value 5
print("Nodes at a distance 2 from the target node:", sol.distanceK(root, target, 2))  # Expected: [7, 4]