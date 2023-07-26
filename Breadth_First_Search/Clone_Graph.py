# Clone Graph: https://leetcode.com/problems/clone-graph/
"""
Time complexity: O(N + M), where N is the number of nodes and M is the number of edges in the graph. This is because we traverse each node and edge once.
Space complexity: O(N), due to the space needed to store the visited information for each node in the graph.
"""


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# O(N+M)  time | O(N) space - where N is the number of nodes and M is the number of edges in the graph
class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val, [])
            visited[node] = clone

            if node.neighbors:
                clone.neighbors = [dfs(n) for n in node.neighbors]

            return clone

        return dfs(node)

# Create a graph for testing
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Test the cloneGraph function
sol = Solution()
clone = sol.cloneGraph(node1)

# Print the adjacency list of the cloned graph
adjacency_list = [[neighbor.val for neighbor in node.neighbors] for node in (clone, clone.neighbors[0], clone.neighbors[1], clone.neighbors[0].neighbors[1])]
print("Adjacency list of the cloned graph:", adjacency_list)  # Expected: [[2, 4], [1, 3], [1, 3], [2, 4]]