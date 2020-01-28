class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 分解p
        p_split = []
        pos = 0
        while(True):
            if pos == len(p):
                break
            if pos == len(p) - 1:
                p_split.append(p[pos])
                break
            if p[pos + 1] == "*":
                p_split.append(p[pos:pos+2])
                pos += 2
            else:
                p_split.append(p[pos])
                pos += 1
        # 逐一字符进行匹配
        return self.match(s, p_split)

    def match(self, s, p):
        if not p and not s:
            return True
        if not p and s:
            return False
        # 匹配.
        if p[0] == ".":
            if len(s) > 0:
                return self.match(s[1:], p[1:])
            else:
                return False
        # 匹配其他字母
        elif len(p[0]) == 1:
            if len(s) > 0 and s[0] == p[0]:
                return self.match(s[1:], p[1:])
            else:
                return False
        # 匹配.*
        elif p[0] == ".*":
            num = 0
            while(num <= len(s)):
                if self.match(s[num:], p[1:]):
                    return True
                num += 1
            return False
        # 匹配a*
        else:
            num = 0
            while(num <= len(s) and (num == 0 or s[num - 1] == p[0][0])):
                if self.match(s[num:], p[1:]):
                    return True
                num += 1
            return False
