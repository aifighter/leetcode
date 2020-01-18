class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = n, n
        current = [('', 0, 0)]
        for i in range(n * 2):
            new_current = []
            for c in current:
                if c[1] > c[2]: # 左括号多，可以添右括号
                    new_current.append((c[0] + ')', c[1], c[2] + 1))
                if c[1] < n: # 左括号有剩余，可以添左括号
                    new_current.append((c[0] + '(', c[1] + 1, c[2]))
            current = new_current
        ret = [c[0] for c in current]
        return ret
        

