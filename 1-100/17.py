class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ret = [""]
        for num in digits[::-1]:
            current = []
            for c in d[num]:
                current += [c + item for item in ret]
            ret = current
        return ret