class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path = [[0 for j in range(n)] for i in range(m)]
        path[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    path[i][j] += path[i - 1][j]
                if j > 0:
                    path[i][j] += path[i][j - 1]
        return path[m - 1][n - 1]