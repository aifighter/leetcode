class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = abs(sum(nums[:3]) - target)
        ret = nums[:3]
        nums = sorted(nums)
        for i, one in enumerate(nums[:-2]):
            left, right = i + 1, len(nums) - 1
            while (left < right):
                two, three = nums[left], nums[right]
                if abs(one + two + three - target) < diff:
                    diff = abs(one + two + three - target)
                    ret = [one, two, three]
                if (one + two + three - target) < 0:
                    left += 1
                elif (one + two + three - target) > 0:
                    right -= 1
                else:
                    return one + two + three
        return sum(ret)