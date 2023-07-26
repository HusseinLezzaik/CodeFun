# Pacific Atlantic Water Flow: https://leetcode.com/problems/pacific-atlantic-water-flow/

# O(mn) time | O(mn) space - where m is the number of rows and n is the number of columns in the matrix
class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(heights), len(heights[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(visited, x, y):
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[nx][ny] or heights[nx][ny] < heights[x][y]:
                    continue
                dfs(visited, nx, ny)

        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n - 1)

        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m - 1, j)

        return [[i, j] for i in range(m) for j in range(n) if p_visited[i][j] and a_visited[i][j]]

# Test the pacificAtlantic function
sol = Solution()
heights = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]
]
print("Cells from which water can flow to both the Pacific and Atlantic oceans:", sol.pacificAtlantic(heights))
# Expected: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
