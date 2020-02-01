class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        prev = [[]]
        for i in range(len(nums)):
            current = []
            for r in prev:
                start = 1 if not r else r[-1] + 1
                end = len(nums)
                for j in range(start, end + 1, 1):
                    current.append(r + [j])
            prev = current
            res += current
        res = [[nums[item - 1] for item in r] for r in res]
        return res