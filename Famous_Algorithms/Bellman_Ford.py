# Bellman-Ford Algorithm

"""
The algorithm works by overestimating the length of the path from the start vertex to all other vertices. Then it iteratively relaxes those estimates by finding new paths that are shorter than the previously overestimated paths.
Bellman-Ford's algorithm is especially useful because it can handle graphs with negative edge weights, unlike other shortest path algorithms such as Dijkstra's algorithm.
"""

"""
Time complexity: Bellman-Ford runs in O(VE) time, where V and E are the number of vertices and edges, respectively. This is because for each node, we traverse its edges, and we do this V-1 times.
Space complexity: The space complexity is O(V), since we need to store a distance for each vertex.
"""

def bellman_ford(graph, source):
    # Step 1: Prepare the distance for each node
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0

    # Step 2: Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:
                # If the distance to the neighbour is lower through this node...
                if distance[node] != float('infinity') and distance[node] + graph[node][neighbour] < distance[neighbour]:
                    # ... then update the distance to that neighbour.
                    distance[neighbour] = distance[node] + graph[node][neighbour]

    # Step 3: Check for negative weight cycles
    for node in graph:
        for neighbour in graph[node]:
            if distance[node] != float('infinity') and distance[node] + graph[node][neighbour] < distance[neighbour]:
                return "Graph contains a negative-weight cycle"

    return distance


# Test cases

# Test case 1: A graph with positive weights
graph_1 = {
    'a': {'b': 1, 'c': 4},
    'b': {'c': 3, 'd': 2, 'e': 2},
    'c': {},
    'd': {'b': 1, 'c': 5},
    'e': {'d': -3}
}
print(bellman_ford(graph_1, 'a'))  # Expected: {'a': 0, 'b': 1, 'c': 4, 'd': 3, 'e': 3}

# Test case 2: A graph with negative weights
graph_2 = {
    'a': {'b': -1, 'c': 4},
    'b': {'c': 3, 'd': 2, 'e': 2},
    'c': {},
    'd': {'b': 1, 'c': 5},
    'e': {'d': -3}
}
print(bellman_ford(graph_2, 'a'))  # Expected: {'a': 0, 'b': -1, 'c': 2, 'd': -2, 'e': 1}

# Test case 3: A graph with a negative cycle
graph_3 = {
    'a': {'b': 1, 'c': 4},
    'b': {'c': 3, 'd': 2, 'e': 2},
    'c': {},
    'd': {'b': -10, 'c': 5},
    'e': {'d': -3}
}
print(bellman_ford(graph_3, 'a'))  # Expected: "Graph contains a negative-weight cycle"