class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        nums = []
        while x > 0:
            nums.append(x % 10)
            x = x // 10
        for i in range(len(nums)):
            if nums[i] != nums[len(nums) - i - 1]:
                return False
        return True