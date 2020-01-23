class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # 检验行
        for row in board:
            if not self.check(row, valid):
                return False
        # 检验列
        for i in range(9):
            col = [row[i] for row in board]
            if not self.check(col, valid):
                return False
        # 检验方格
        for i in range(3):
            for j in range(3):
                square = []
                for m in range(3):
                    for n in range(3):
                        square.append(board[i * 3 + m][j * 3 + n])
                if not self.check(square, valid):
                    return False
        return True

    def check(self, l, valid):
        show = []
        for num in l:
            if num == ".":
                continue
            elif num in valid:
                if num in show:
                    return False
                else:
                    show.append(num)
            else:
                return False
        return True