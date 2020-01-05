class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        if len(nums) < 4:
            return ret
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            three = self.threeSum(nums[i + 1:], target - nums[i])
            if three:
                for t in three:
                    if [nums[i]] + t not in ret:
                        ret.append([nums[i]] + t)
        return ret



    def threeSum(self, nums, target):
            nums.sort()
            res =[]
            i = 0
            for i in range(len(nums)):
                if i == 0 or nums[i]>nums[i-1]:
                    l = i+1
                    r = len(nums)-1
                    while l < r:
                        s = nums[i] + nums[l] +nums[r]
                        if s == target:
                            res.append([nums[i],nums[l],nums[r]])
                            l +=1
                            r -=1
                            while l < r and nums[l] == nums[l-1]:
                                l += 1
                            while r > l and nums[r] == nums[r+1]:
                                r -= 1
                        elif s > target:
                            r -=1
                        else :
                            l +=1
            return res