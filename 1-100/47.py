class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)
        
    def helper(self, nums):
        if len(nums) == 1:
            return [nums]
        ret = []
        show = []
        for i in range(len(nums)):
            new_nums = nums.copy()
            n = new_nums.pop(i)
            if n in show:
                continue
            show.append(n)
            prev = self.helper(new_nums)
            ret += [[n] + p for p in prev]
        return ret