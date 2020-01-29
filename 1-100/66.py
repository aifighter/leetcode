class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        prev = 1
        for d in digits[::-1]:
            d += prev
            if d == 10:
                ret.append(0)
                prev = 1
            else:
                ret.append(d)
                prev = 0
        if prev == 1:
            ret.append(prev)
        return ret[::-1]