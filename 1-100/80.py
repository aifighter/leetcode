class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        l = 2
        prev = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            new_prev = [prev[1], nums[i]]
            if nums[i] != prev[0] or nums[i] != prev[1]:
                nums[l] = nums[i]
                l += 1
            prev = new_prev
        return l