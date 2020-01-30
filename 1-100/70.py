class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {1:1, 2:2})

    def helper(self, n, cache):
        if n in cache:
            return cache[n]
        cache[n] = self.helper(n - 1, cache) + self.helper(n - 2, cache)
        return cache[n]