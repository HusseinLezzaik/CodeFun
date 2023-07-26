# Number of Islands: https://leetcode.com/problems/number-of-islands/
"""
Time complexity: O(M * N), where M and N are the number of rows and columns respectively in the grid. This is because in the worst case we may need to visit every cell in the grid.
Space complexity: O(M * N), due to the space needed for the DFS stack in the worst case scenario when the grid map is filled with lands where DFS goes by M * N deep.
"""


# O(M * N) time | O(M * N) space - where M and N are the number of rows and columns respectively in the grid
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

# Test the numIslands function
sol = Solution()
grid = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0']
]
print("Number of islands:", sol.numIslands(grid))  # Expected: 1