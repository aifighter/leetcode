class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 特殊情况
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        # 二分查找并保存所有的target的idx
        results = []
        self.findnum(nums, 0, len(nums), target, results)
        if not results:
            return [-1, -1]
        else:
            return [min(results), max(results)]
            

    def findnum(self, nums, start, end, target, results):
        if target > nums[end - 1] or target < nums[start]:
            return
        if start + 1 == end:
            if nums[start] == target:
                results.append(start)
                return
            else:
                return
        mid = (start + end) // 2
        self.findnum(nums, start, mid, target, results);
        self.findnum(nums, mid, end, target, results);