class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left, right, ret = 0, 0, 0
        while(True):
            if left == len(s) or right == len(s):
                break
            if s[right] not in d:
                d[s[right]] = 1
                right += 1
            else:
                while(s[left] != s[right]):
                    del d[s[left]]
                    left += 1
                del d[s[left]]
                left += 1
            if len(d) > ret:
                ret = len(d)
        return ret
