class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.cache = {}
        return self.helper(s1, s2, s3)
        

    def helper(self, s1, s2, s3):
        # cache
        if (s1, s2, s3) in self.cache:
            return self.cache[(s1, s2, s3)]
        # 所有边缘条件，屌爆了
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        # 主体
        if s1[0] == s3[0] and self.helper(s1[1:], s2, s3[1:]):
            res = True
        elif s2[0] == s3[0] and self.helper(s1, s2[1:], s3[1:]):
            res = True
        else:
            res = False
        self.cache[(s1, s2, s3)] = res
        return res
        

