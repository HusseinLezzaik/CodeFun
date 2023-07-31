# Breadth First Search

class Graph:
    def __init__(self):
        self.graph = {}

# O(V+E) time | O(V) space - where V is the number of vertices and E is the number of edges in the input graph
from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# usage:
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
bfs(graph, 'A')  # A -> B -> C -> D -> E -> F

