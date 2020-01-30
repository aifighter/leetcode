class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            zero = False
            for j in range(n):
                if matrix[i][j] == 0:
                    zero = True
                    break
            if zero:
                for j in range(n):
                    if matrix[i][j] != 0:
                        matrix[i][j] = None
        for j in range(n):
            zero = False
            for i in range(m):
                if matrix[i][j] == 0:
                    zero = True
                    break
            if zero:
                for i in range(m):
                    if matrix[i][j] != 0:
                        matrix[i][j] = None
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        