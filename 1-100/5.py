class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        ret = s[0]
        for i in range(len(s)):
            word = s[i]
            move = 1
            while(True):
                if i - move < 0 or i + move >= len(s):
                    break
                if s[i - move] == s[i + move]:
                    word = s[i-move: i+move+1]
                    if len(word) > len(ret):
                        ret = word
                else:
                    break
                move += 1
            word = ""
            move = 0
            while(True):
                if i - move < 0 or i + move + 1 >= len(s):
                    break
                if s[i - move] == s[i + move + 1]:
                    word = s[i-move: i+move+2]
                    if len(word) > len(ret):
                        ret = word
                else:
                    break
                move += 1
        return ret