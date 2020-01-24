class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)

    def helper(self, nums):
        if len(nums) == 1:
            return [nums]
        ret = []
        for i in range(len(nums)):
            new_nums = nums.copy()
            n = new_nums.pop(i)
            prev = self.helper(new_nums)
            ret += [[n] + p for p in prev]
        return ret