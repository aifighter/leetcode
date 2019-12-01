class Solution:
    def reverse(self, x: int) -> int:
        ret = None
        s = str(x)
        if s[0] == '-':
            ret = -1 * int(s[1:][::-1])
        else:
            ret = int(s[::-1])
        if ret < - 2 ** 31 or ret > 2 ** 31 - 1:
            return 0
        return ret