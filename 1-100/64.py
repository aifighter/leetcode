class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        path = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    path[i][j] = grid[i][j] + min(path[i - 1][j], path[i][j - 1])
                elif i > 0:
                    path[i][j] = grid[i][j] + path[i - 1][j]
                elif j > 0:
                    path[i][j] = grid[i][j] + path[i][j -  1]
                else:
                    path[i][j] = grid[i][j]
        return path[m - 1][n - 1]