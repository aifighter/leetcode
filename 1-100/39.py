class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = self.helper(candidates, target)
        ret = [list(item) for item in ret]
        return ret

    def helper(self, candidates, target):
        ret = set()
        for c in candidates:
            if c == target:
                ret.add((c, ))
            if c > target:
                continue
            if c < target:
                for group in self.helper(candidates, target - c):
                    new_group = [c] + list(group)
                    new_group = tuple(sorted(new_group))
                    ret.add(new_group)
        return ret