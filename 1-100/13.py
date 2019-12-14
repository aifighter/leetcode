class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ret = 0
        prev = 0
        for alpha in s[::-1]:
            num = d[alpha]
            if num < prev:
                ret -= num
            else:
                ret += num
            prev = num
        return ret