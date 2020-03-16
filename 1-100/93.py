class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.helper(s, 4, "")
        return self.res

    def helper(self, s, n, before):
        if n < 0:
            return
        if n == 0 and len(s) == 0:
            self.res.append(before[1:])
        if len(s) >= 1:
            self.helper(s[1:], n - 1, before + "." + s[:1])
        if len(s) >= 2 and s[0] != '0':
            self.helper(s[2:], n - 1, before + "." + s[:2])
        if len(s) >= 3 and int(s[:3]) <= 255 and s[0] != '0':
            self.helper(s[3:], n - 1, before + "." + s[:3])