class Solution:
    def intToRoman(self, num: int) -> str:
        ge = ['', 'I','II','III','IV','V','VI','VII','VIII','IX']
        shi = [s.replace('X', 'C').replace('V', 'L').replace('I', 'X') for s in ge]
        bai = [s.replace('X', 'M').replace('V', 'D').replace('I', 'C') for s in ge]
        q, b, s, g = num // 1000, (num % 1000) // 100, (num % 100) // 10, num % 10
        return "M" * q + bai[b] + shi[s] + ge[g]