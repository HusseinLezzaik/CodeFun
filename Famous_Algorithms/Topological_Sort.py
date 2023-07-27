"""
Topological Sort Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, 
vertex u comes before v in the ordering.
Topological Sorting for a graph is not possible if the graph is not a DAG.

"""

from collections import defaultdict, deque

"""
The time complexity is O(V+E), where V is the number of vertices and E is the number of edges.
This is because we visit each node and edge once.

The space complexity is O(V), because we store the graph (both the adjacency list and in-degrees array) and the result.
In the worst case, if all nodes are in the queue, the space complexity will be O(V).
"""

def topological_sort(n, edges):
    adj_list = defaultdict(list)
    indegrees = [0] * n
    for u, v in edges:
        adj_list[u].append(v)
        indegrees[v] += 1

    # Initialize queue with nodes having 0 in-degree
    q = deque([u for u in range(n) if indegrees[u] == 0])

    result = []
    while q:
        node = q.popleft()
        result.append(node)

        # Reduce in-degrees of neighbors
        for neighbor in adj_list[node]:
            indegrees[neighbor] -= 1
            # If in-degree becomes 0, add it to queue
            if indegrees[neighbor] == 0:
                q.append(neighbor)

    return result if len(result) == n else []

# Test cases
print(topological_sort(2, [[1, 0]]))  # Output: [1, 0]
print(topological_sort(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [2, 1, 0, 3]
