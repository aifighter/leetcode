class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ret = []
        m, n = len(matrix), len(matrix[0])
        used = [[0 for j in range(n)] for i in range(m)]
        i, j = 0, 0
        states = ["right", "down", "left", "up"]
        state = 0
        cnt = 0
        while(cnt < m * n):
            ret.append(matrix[i][j])
            used[i][j] = 1
            if state == 0:
                if j + 1 < n and (not used[i][j + 1]):
                    i, j = i, j + 1
                else:
                    state = 1
                    i, j = i + 1, j
            elif state == 1:
                if i + 1 < m and (not used[i + 1][j]):
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
            cnt += 1
        return ret