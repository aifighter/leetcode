class Solution:
    def myAtoi(self, str: str) -> int:
        # 找到开头的数
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        start = 0
        while start < len(str) and str[start] == ' ':
            start += 1
        if start == len(str):
            return 0
        if str[start] not in nums + ['-', '+']:
            return 0
        # 找到结尾的数
        end = start + 1
        while end < len(str) and str[end] in nums:
            end += 1
        num = str[start: end]
        if num == '-' or num == '+':
            return 0
        else:
            num = int(num)
        if num > 2 ** 31 - 1:
            num = 2 ** 31 - 1
        if num < - 2 ** 31:
            num = - 2 ** 31
        return num
