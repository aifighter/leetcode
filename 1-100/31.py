class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        current_max = nums[-1]
        idx = None
        # 先找到后面有更大数的那一位
        for i in range(n):
            if nums[n - i - 1] >= current_max:
                current_max = nums[n - i - 1]
            else:
                idx = n - i - 1
                break
        # 如果是递减序列，那么重新排序并返回
        if idx is None:
            nums.sort()
            return
        # 从该位数后面找最小的那个数
        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
        # 对交换后的后面部分进行排序
        s = sorted(nums[idx + 1:])
        nums[idx + 1:] = s
        return