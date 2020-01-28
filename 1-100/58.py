class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s[::-1]
        num = 0
        for i in range(len(s)):
            if self.helper(s[i]):
                j = i
                while(j < len(s)):
                    if self.helper(s[j]):
                        num += 1
                        j += 1
                    else:
                        break
                break
        return num
    
    def helper(self, c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'