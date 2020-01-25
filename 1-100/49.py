class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        ret = []
        for word in strs:
            letters = tuple(sorted(word))
            if letters in d:
                d[letters].append(word)
            else:
                d[letters] = [word]
        for key in d:
            ret.append(d[key])
        return ret