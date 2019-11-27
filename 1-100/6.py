class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ['' for i in range(numRows)]
        for i, c in enumerate(s):
            idx = i % (numRows * 2 - 2)
            if idx < numRows:
                rows[idx] += c
            else:
                rows[numRows * 2 - idx - 2] += c
        ret = ''.join(rows)
        return ret