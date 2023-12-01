# Network Delay Time: https://leetcode.com/problems/network-delay-time/
"""
the main lesson from this question is to practice using Dijkstra's algorithm to find the shortest path.

"""


import collections
import heapq

# O(NlogN) time | O(N) space - where N is the number of edges in the graph
def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    distance = {node: float('inf') for node in range(1, N+1)}
    distance[K] = 0
    heap = [(0, K)]

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distance[node]:
            continue
        for nei, d in graph[node]:
            new_distance = dist + d
            if new_distance < distance[nei]:
                distance[nei] = new_distance
                heapq.heappush(heap, (new_distance, nei))

    max_dist = max(distance.values())
    return max_dist if max_dist < float('inf') else -1

# Test the networkDelayTime function
print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # Expected: 2
print(networkDelayTime([[1, 2, 1]], 2, 2))  # Expected: -1
print(networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))  # Expected: 3
print(networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1))  # Expected: 3
