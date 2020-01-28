class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1, 1))
        ret = ""
        k = k - 1
        for i in range(n):
            num, k = self.helper(nums, k)
            ret += str(num)
            nums.remove(num)
        return ret

    def helper(self, nums, k):
        tmp = self.jiechen(len(nums) - 1)
        return nums[k // tmp], k % tmp
    
    def jiechen(self, n):
        ret = 1
        for i in range(n):
            ret *= (i + 1)
        return ret