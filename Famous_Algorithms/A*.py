"""
A* (A-star) is a popular pathfinding algorithm used in many fields, including computer games and logistics.
Like Dijkstra's Algorithm, it's used to find the shortest path between two nodes in a graph. 
But unlike Dijkstra's Algorithm, which explores all possible paths, A* uses a heuristic to estimate the cost from the current node to the goal, 
allowing it to focus on promising paths and often finding the shortest path more quickly.

The time complexity of the A* algorithm is O(E+VlogV), where E is the number of edges and V is the number of vertices.
This is because each node is inserted into the priority queue once for each edge that leads to it, and each insertion takes logV time. 

The space complexity is O(V), as in the worst case we might need to store every node in the queue, the came_from dictionary, and the cost_so_far dictionary.

"""

import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Node({self.x}, {self.y})"


class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.counter = 0

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, self.counter, item))
        self.counter += 1

    def get(self):
        return heapq.heappop(self.elements)[2]


def heuristic(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls

    def neighbors(self, node):
        neighbors = [Node(node.x+1, node.y), Node(node.x-1, node.y), Node(node.x, node.y-1), Node(node.x, node.y+1)]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def cost(self, from_node, to_node):
        return 1 if self.passable(to_node) else float('inf')


# Define a 10x10 grid
grid = Grid(10, 10)

# Define some walls
grid.walls = [Node(1, 3), Node(1, 4), Node(1, 5), Node(2, 5), Node(3, 5), Node(4, 5), Node(5, 5), Node(6, 5)]

# Define the start and goal
start = Node(0, 0)
goal = Node(9, 9)

# Run the A* search
came_from, cost_so_far = a_star_search(grid, start, goal)

# Print the path from start to goal
current = goal
path = []
while current != start:
    path.append(current)
    current = came_from[current]
path.append(start)
path.reverse()
path
