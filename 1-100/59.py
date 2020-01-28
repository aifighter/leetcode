class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0 for i in range(n)] for j in range(n)]
        used = [[0 for i in range(n)] for j in range(n)]
        state = 0
        i, j = 0, 0
        for idx in range(n * n):
            ret[i][j] = idx + 1
            used[i][j] = 1
            if state == 0:
                if j + 1 < n and (not used[i][j + 1]):
                    i, j = i, j + 1
                else:
                    state = 1
                    i, j = i + 1, j
            elif state == 1:
                if i + 1 < n and (not used[i + 1][j]):
                    i, j = i + 1, j
                else:
                    state = 2
                    i, j = i, j - 1
            elif state == 2:
                if j - 1 >= 0 and (not used[i][j - 1]):
                    i, j = i, j - 1
                else:
                    state = 3
                    i, j = i - 1, j
            elif state == 3:
                if i - 1 >= 0 and (not used[i - 1][j]):
                    i, j = i - 1, j
                else:
                    state = 0
                    i, j = i, j + 1
        return ret