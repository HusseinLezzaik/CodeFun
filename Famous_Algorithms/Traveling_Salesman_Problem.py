# The Traveling Salesman Problem (TSP) is a classic problem in combinatorial optimization.
"""
Note: The graph representing the cities and distances is assumed to be complete (i.e., every pair of distinct vertices is connected by a unique edge) and undirected (i.e., the distance from city i to city j is the same as the distance from city j to city i).
The tsp function takes as input a 2D array graph where graph[i][j] is the distance from city i to city j. The function returns the minimum total distance of a route that visits each city exactly once and returns to the origin city.
"""

"""
Time complexity of O(n^2*2^n) 
Space Complexity ofO(n*2^n)  
where n is the number of cities.
"""

from itertools import combinations

def tsp(graph):
    N = len(graph)
    dp = [[float('inf')] * (1 << N) for _ in range(N)]
    dp[0][1] = 0

    for mask in range(1, 1 << N):
        for submask in combinations(range(N), bin(mask).count('1')):
            submask = (0,) + submask
            mask_val = sum(1 << i for i in submask)
            if mask_val != mask:
                continue

            for i, j in combinations(submask, 2):
                without_ij = mask_val ^ (1 << i) ^ (1 << j)
                for k in submask:
                    if k == i or k == j:
                        continue
                    dp[i][mask_val] = min(dp[i][mask_val], dp[k][without_ij] + graph[k][i])
                    dp[j][mask_val] = min(dp[j][mask_val], dp[k][without_ij] + graph[k][j])

    return min(dp[i][(1 << N) - 1] + graph[i][0] for i in range(N))


graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(tsp(graph))  # Output: 80