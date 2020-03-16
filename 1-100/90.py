class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = [[[]]]
        for i in range(len(nums)):
            new_subset = []
            for j in range(len(res)):
                subset = res[len(res) - j - 1]
                if j == 0:
                    target_set = []
                else:
                    target_set = res[len(res) - j]
                for item in subset:
                    new_item = item + [nums[i]]
                    if new_item not in target_set:
                        target_set.append(new_item)
                if j == 0:
                    new_subset = target_set
            res.append(new_subset)
        new_res = []
        for subset in res:
            new_res += subset
        return new_res