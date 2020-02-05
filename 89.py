class Solution:
    def grayCode(self, n: int) -> List[int]:
        prev = [False for i in range(n)]
        greg = [prev]
        ret = [0]
        for i in range(2 ** n - 1):
            current = prev.copy()
            for i in range(n):
                current[i] = not current[i]
                if current not in greg:
                    greg.append(current)
                    prev = current
                    num = 0
                    for x in range(n):
                        num += current[x] * (2 ** x)
                    ret.append(num)
                    break
                else:
                    current[i] = not current[i]
        return ret