class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for idx in range(k):
            new_res = []
            for r in res:
                start = 1 if not r else r[-1] + 1
                end = n - k + 1 + idx
                for num in range(start, end + 1):
                    new_res.append(r + [num])
            res = new_res
        return res