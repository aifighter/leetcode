class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while True:
            if left * left == x:
                return left
            if right * right == x:
                return right
            if left + 1 == right:
                return left
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            else:
                right = mid