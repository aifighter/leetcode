class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 特殊情况优先判断
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
        # 先将数组恢复成升序排列
        split = self.findmid(nums, 0, len(nums) - 1)
        nums = nums[split:] + nums[:split]
        # 再使用二分法找到对应位置
        idx = self.findnum(nums, 0, len(nums), target)
        if idx is None:
            return False
        else:
            return True

    def findnum(self, nums, start, end, target):
        if end - start == 1:
            if nums[start] == target:
                return start
            else:
                return None
        mid = (start + end) // 2
        left = self.findnum(nums, start, mid, target)
        right = self.findnum(nums, mid, end, target)
        if left is not None:
            return left
        if right is not None:
            return right
        return None
    
    def findmid(self, nums, start, end):
        if start + 1 == end:
            if nums[start] <= nums[end]:
                return 0
            else:
                return end
        mid = (start + end) // 2
        return self.findmid(nums, start, mid) + self.findmid(nums, mid, end)