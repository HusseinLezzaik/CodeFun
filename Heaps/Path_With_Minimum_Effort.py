# Path with Minimum Effort: https://leetcode.com/problems/path-with-minimum-effort/
"""
The time complexity is O(mxnxlog(mxn)), where m and n are the number of rows and columns in the heights array.
This is because in the worst case, we need to visit each cell once and each operation in the heap takes O(log(mxn)) time.

The space complexity is O(mxn), because we store the distance for each cell in the dist array and in the worst case, all the cells could be in the heap.
"""

from typing import List

def minimumEffortPath(heights: List[List[int]]) -> int:
    import heapq
    m, n = len(heights), len(heights[0])
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    heap = [(0, 0, 0)] # distance, row, col
    while heap:
        d, r, c = heapq.heappop(heap)
        if d != dist[r][c]:
            continue
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                if dist[nr][nc] > nd:
                    dist[nr][nc] = nd
                    heapq.heappush(heap, (nd, nr, nc))
    return dist[m-1][n-1]


print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))  # Expected output: 2