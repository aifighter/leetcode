class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        current = 0
        while(True):
            further = False
            far = current + nums[current]
            for i in range(current, min(len(nums), current + nums[current] + 1), 1):
                if i + nums[i] > far:
                    far = i + nums[i]
                    current = i
                    further = True
            if far >= len(nums) - 1:
                return True
            if not further:
                return False