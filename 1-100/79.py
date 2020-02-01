class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if board == [] or board == [[]]:
            return False
        m, n = len(board), len(board[0])
        used = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if self.walk(i, j, word, board, used):
                    return True
        return False
        
    def walk(self, row, col, word, board, used):
        if not word:
            return True
        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return False
        if word[0] != board[row][col]:
            return False
        if used[row][col]:
            return False
        for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            used[row][col] = 1
            if self.walk(r, c, word[1:], board, used):
                return True
            used[row][col] = 0
        return False