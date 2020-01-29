class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, c = a[::-1], b[::-1], ""
        prev = 0
        for i in range(max(len(a), len(b))):
            aa = 0 if i >= len(a) else int(a[i])
            bb = 0 if i >= len(b) else int(b[i])
            cc = aa + bb + prev
            if cc >= 2:
                c += str(cc % 2)
                prev = 1
            else:
                c += str(cc)
                prev = 0
        if prev == 1:
            c += str(prev)
        return c[::-1]