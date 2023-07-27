# Path With Maximum Probability: https://leetcode.com/problems/path-with-maximum-probability/

"""
The time complexity is O(ElogE), where E is the number of edges. This is because we process each edge once and each operation in the priority queue takes logarithmic time.

The space complexity is O(N+E), where N is the number of nodes. This is because we store the graph as an adjacency list.
"""

import heapq
from collections import defaultdict

def maxProbability(n, edges, succProb, start, end):
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        graph[a].append((b, succProb[i]))
        graph[b].append((a, succProb[i]))

    max_prob = [0] * n
    max_prob[start] = 1
    pq = [(-1, start)]

    while pq:
        prob, node = heapq.heappop(pq)
        prob = -prob
        if prob < max_prob[node]:
            continue
        for nei, succ in graph[node]:
            if prob * succ > max_prob[nei]:
                max_prob[nei] = prob * succ
                heapq.heappush(pq, (-max_prob[nei], nei))

    return max_prob[end]

print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))  # Expected output: 0.25