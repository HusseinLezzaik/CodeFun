# Find the City with the Smallest Number of Neighbors at a Threshold Distance: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

"""
The time complexity is O(n^3)  because the Floyd-Warshall algorithm takes cubic time.

The space complexity is O(n^2)  because we store the graph as an adjacency matrix.
"""

def findTheCity(n, edges, distanceThreshold):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i, j, w in edges:
        dist[i][j] = dist[j][i] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    min_neigh = float('inf')
    ans = -1
    for i in range(n-1, -1, -1):
        neigh = sum(d <= distanceThreshold for d in dist[i])
        if neigh <= min_neigh:
            min_neigh = neigh
            ans = i
    return ans


print(findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))  # Expected output: 0