# Dijsktra's Algorithm

"""
Dijkstra's algorithm is a graph search algorithm that solves the shortest path problem for a graph with non-negative edge path costs,
producing a shortest path tree.

The algorithm uses a priority queue data structure to select the next vertex to explore.

The time complexity of Dijkstra's algorithm using a binary heap is O((V+E)logV), where V is the number of vertices and E is the number of edges.
This is because for each node, we might have to update (using decrease key operation) and/or insert into the priority queue. Both these operations are O(logV), 
and we may have to do them for each edge (in the worst case). Therefore, the time complexity is O((V+E)logV).

This can be improved to O(E+VlogV) using a Fibonacci heap, but such an implementation is more complex and the constant factors are typically larger.


"""
# Each node in the graph is represented as a dictionary where the keys are the neighbors of the node and the values are the edge weights between the node and its neighbors.
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight


import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Important check to decrease time complexity
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it is shorter than any path we have already found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2},
    'C': {'A': 3, 'B': 2}
}

# Run Dijkstra's algorithm on the example graph with 'A' as the starting node
dijkstra(graph, 'A') # Result: {'A': 0, 'B': 1, 'C': 3}