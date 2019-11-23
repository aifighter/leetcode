class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        index_sorted = sorted(range(len(nums)), key=lambda x: nums[x])
        i, j = 0, len(nums) - 1
        while(True):
            if nums_sorted[i] + nums_sorted[j] < target:
                i += 1
            elif nums_sorted[i] + nums_sorted[j] > target:
                j -= 1
            else:
                return [index_sorted[i], index_sorted[j]]
            