class Solution:
    def numDecodings(self, s: str) -> int:
        self.cache = {}
        return self.helper(s)

    def helper(self, s):
        if s in self.cache:
            return self.cache[s]
        if s[0] == '0':
            res = 0
        elif len(s) == 1:
            res = 1
        elif len(s) == 2 and 1 <= int(s) <= 26:
            res = 1 + self.helper(s[1:])
        elif 1 <= int(s[:2]) <= 26:
            res = self.helper(s[1:]) + self.helper(s[2:])
        else:
            res = self.helper(s[1:])
        self.cache[s] = res
        return res