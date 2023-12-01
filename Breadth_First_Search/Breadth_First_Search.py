# Breadth First Search
"""
questions that often involve using BFS are ones that involve finding the shortest path between two nodes in a graph.
and also often involve using a queue.

the trick with queues is that you're often looking for something, and you want to check the things closest to it first.
and then you want to keep track of the other things you've yet to check, so you apend them inside a queue.

usually when the queue is empty that means we can stop. 

btw in python u can initialize a queue with the root of a BT like this: queue = collections.deque([root])
"""


class Graph:
    def __init__(self):
        self.graph = {}

# O(V+E) time | O(V) space - where V is the number of vertices and E is the number of edges in the input graph
def breadth_first_search(graph, start):
    """
    Perform a breadth-first search on a graph.

    :param graph: A dictionary representing the graph, where keys are node ids and values are lists of adjacent node ids.
    :param start: The node id to start the BFS from.
    :return: A list of nodes in the order they were visited.
    """
    visited = []  # List to keep track of visited nodes.
    queue = []    # Initialize a queue

    visited.append(start)
    queue.append(start)

    while queue:          # Creating loop to visit each node
        m = queue.pop(0) 
        print(m, end = " ") 

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

"""
  A
 / \
B   C
|   |
D   E
 \ /
  F

Breadth First Search Order: ['A', 'B', 'C', 'D', 'E', 'F']
"""

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS starting from 'A':")
bfs(graph, 'A')


