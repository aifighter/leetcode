class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(candidates, target, {})

    def helper(self, candidates, target, cache):
        if (tuple(candidates), target) in cache:
            return cache[(tuple(candidates), target)]
        ret = []
        for i in range(len(candidates)):
            new_c = candidates.copy()
            num = new_c.pop(i)
            if num == target:
                ret.append([target])
            if num > target:
                continue
            if num < target:
                prev = self.helper(new_c, target - num, cache)
                ret += [p + [num] for p in prev] 
        ret = set([tuple(sorted(r)) for r in ret])
        ret = [list(r) for r in list(ret)]
        cache[(tuple(candidates), target)] = ret
        return ret