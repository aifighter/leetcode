class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_l = len(nums1) + len(nums2)
        if total_l % 2 == 1:
            return self.helper(nums1, nums2, total_l // 2)
        else:
            return (self.helper(nums1, nums2, total_l // 2 - 1) + self.helper(nums1, nums2, total_l // 2)) / 2.0

    # 找到nums1和nums2中第n大的数（n从0开始）
    def helper(self, nums1, nums2, n):
        # 让nums1是更短的那个数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # 当一个数组为空时
        if not nums1:
            return nums2[n]
        # 当一个数组长度为1时，为了避免死循环，直接想办法return
        if len(nums1) == 1:
            if n == 0:
                return min(nums1[0], nums2[0])
            if n == len(nums1) + len(nums2) - 1:
                return max(nums1[0], nums2[-1])
            if nums2[n] <= nums1[0]:
                return nums2[n]
            if nums2[n - 1] <= nums1[0]:
                return nums1[0]
            else:
                return nums2[n - 1]
        # 当两个数组都不为空时，砍掉一个数组的一半
        mid = (len(nums1) + len(nums2)) // 2
        mid1, mid2 = len(nums1) // 2, len(nums2) // 2
        median1, median2 = self.median(nums1), self.median(nums2)
        if n < mid:
            if median1 < median2:
                return self.helper(nums1, nums2[:mid2], n)
            else:
                return self.helper(nums1[:mid1], nums2, n)
        else:
            if median1 < median2:
                return self.helper(nums1[mid1:], nums2, n - mid1)
            else:
                return self.helper(nums1, nums2[mid2:], n - mid2)

    def median(self, nums):
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2.0
