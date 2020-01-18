class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        pair = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c != pair[stack[-1]]:
                    return False
                else:
                    stack = stack[:-1]
        if not stack:
            return True
        else:
            return False