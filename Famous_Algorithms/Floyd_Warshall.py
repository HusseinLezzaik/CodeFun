# Floyd Warshall Algorithm

"""
The time complexity of the Floyd-Warshall algorithm is O(n^3), where n is the number of vertices in the graph.
This is because the algorithm has three nested loops: one for each vertex as the intermediate vertex, one for each vertex as the source vertex, and one for each vertex as the destination vertex.

The space complexity of the Floyd-Warshall algorithm is O(n^2), where n is the number of vertices in the graph. This is because we need a 2D matrix to store the shortest distances between every pair of vertices. Each row in the matrix represents a source vertex and each column in the matrix represents a destination vertex. 
Therefore, for n vertices, we will have O(nxn) entries in the matrix.

"""


def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i, j, w in edges:
        dist[i][j] = dist[j][i] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Test cases
print(floyd_warshall(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1]]))
print(floyd_warshall(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]))