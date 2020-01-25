class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n % 2 == 0:
            row = n // 2
            col = n // 2
        else:
            row = n // 2
            col = n // 2 + 1
        for i in range(row):
            for j in range(col):
                matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j], matrix[n-1-j][i] = \
                matrix[n-1-j][i], matrix[i][j], matrix[j][n-1-i], matrix[n-1-i][n-1-j]
        return matrix