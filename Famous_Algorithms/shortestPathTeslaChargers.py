"""
Shortest Path in Tesla Chargers:
Given a map of Tesla chargers and distances between them, find the shortest path between two chargers
"""

import heapq
from typing import Dict, List, Tuple

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, from_node: str, to_node: str, distance: int):
        if from_node not in self.nodes:
            self.nodes[from_node] = {}
        self.nodes[from_node][to_node] = distance

def dijkstra(graph: Graph, start: str, end: str) -> Tuple[int, List[str]]:
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    pq = [(0, start)]
    previous = {node: None for node in graph.nodes}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            return current_distance, path[::-1]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.nodes[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return float('infinity'), []

# Example usage
g = Graph()
g.add_edge("ChargerA", "CityB", 5)
g.add_edge("CityB", "ChargerC", 15)
g.add_edge("ChargerA", "CityD", 12)
g.add_edge("CityD", "ChargerC", 3)
g.add_edge("CityB", "CityD", 4)

start_charger = "ChargerA"
end_charger = "ChargerC"

distance, path = dijkstra(g, start_charger, end_charger)
print(f"Shortest distance from {start_charger} to {end_charger}: {distance}")
print(f"Path: {' -> '.join(path)}")