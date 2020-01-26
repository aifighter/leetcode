class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        ret = 0
        left, right = 0, 1
        current_sum = 0
        while(right <= len(nums)):
            current_sum += nums[right - 1]
            if current_sum < 0:
                left = right
                right += 1
                current_sum = 0
            else:
                ret = max(ret, current_sum)
                right += 1
        return ret