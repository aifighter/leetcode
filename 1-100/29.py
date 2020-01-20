class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 特殊情况
        if dividend == - (2 ** 31) and divisor == -1:
            return 2 ** 31 - 1 
        # 先判断符号，再转换成正数做除法
        multiply = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            multiply = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        # 从高位向低位做除法
        ret = ''
        prev = '0'
        for num in str(dividend):
            x = int(prev + num)
            y = int(abs(divisor))
            z = 0
            while x >= y:
                x -= y
                z += 1
            ret += str(z)
            prev = str(x)
        if multiply == 1:
            return int(ret)
        else:
            return int('-' + ret)

