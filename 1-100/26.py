class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num = None
        idx = 0
        for i in range(len(nums)):
            if nums[i] != num:
                nums[idx] = nums[i]
                num = nums[i]
                idx += 1
        return idx