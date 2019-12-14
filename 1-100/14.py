class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ret = strs[0]
        for s in strs[1:]:
            ret = self.helper(ret, s)
        return ret
    def helper(self, a, b):
        l = min(len(a), len(b))
        start, end = 0, l
        while(start < end):
            curr = (start + end) // 2
            if start == curr:
                if a[:end] == b[:end]:
                    return a[:end]
                else:
                    return a[:start]
            if a[:curr] == b[:curr]:
                start = curr
            else:
                end = curr
        return ""