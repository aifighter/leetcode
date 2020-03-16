class Solution:
    def numTrees(self, n: int) -> int:
        self.cache = {}
        return self.helper(n)

    def helper(self, n):
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            res = 1
        else:
            res = 0
            for i in range(n):
                res += self.helper(i) * self.helper(n - 1 - i)
        self.cache[n] = res
        return res