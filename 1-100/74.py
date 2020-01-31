class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]]:
            return False
        if matrix == []:
            return False
        col = [row[0] for row in matrix]
        result, idx = self.helper(col, target)
        if idx == -1:
            return False
        row = matrix[idx]
        result, idx = self.helper(row, target)
        return result

    def helper(self, nums, target):
        left, right = 0, len(nums) - 1
        while 1:
            if nums[left] > target:
                return False, left
            if nums[right] < target:
                return False, right
            if nums[left] == target:
                return True, left
            if nums[right] == target:
                return True, right
            if left + 1 == right:
                return False, left
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid