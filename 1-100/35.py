class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == target:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        return self.helper(nums, 0, len(nums) - 1, target)

    def helper(self, nums, start, end, target):
        if nums[start] > target or nums[end] < target:
            return None
        if start + 1 == end:
            if target == nums[start]:
                return start
            if target == nums[end]:
                return end
            if nums[start] < target < nums[end]:
                return end
            return None
        mid = (start + end) // 2
        left_ret = self.helper(nums, start, mid, target)
        right_ret = self.helper(nums, mid, end, target)
        if left_ret is not None:
            return left_ret
        if right_ret is not None:
            return right_ret
        return None