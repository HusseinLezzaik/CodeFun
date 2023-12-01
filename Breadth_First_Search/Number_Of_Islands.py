# Number of Islands: https://leetcode.com/problems/number-of-islands/
"""
Time complexity: O(M * N), where M and N are the number of rows and columns respectively in the grid. This is because in the worst case we may need to visit every cell in the grid.
Space complexity: O(M * N), due to the space needed for the DFS stack in the worst case scenario when the grid map is filled with lands where DFS goes by M * N deep.

Grpah Problem:
many graph problems build on top of this one, and it's quite common queston in interviews.
the trick is to use DFS to find connected components and count them. note that we use rows/columns to track what has been visited.

hashtable and set are also useful for graph problems to track what has been visited.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Version From Video
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

         def bfs(r,c):
             q = deque()
             visited.add((r,c))
             q.append((r,c))
           
             while q:
                 row,col = q.popleft()
                 directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                 for dr,dc in directions:
                     r,c = row + dr, col + dc
                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                         q.append((r , c ))
                         visited.add((r, c ))

         for r in range(rows):
             for c in range(cols):
               
                 if grid[r][c] == "1" and (r,c) not in visited:
                     bfs(r,c)
                     islands +=1 

         return islands



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