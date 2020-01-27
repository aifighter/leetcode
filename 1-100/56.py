class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        ret = []
        intervals = sorted(intervals, key=lambda x:x[0])
        current = intervals[0]
        for inte in intervals:
            if inte[0] <= current[1]:
                current[1] = max(inte[1], current[1])
            else:
                ret.append(current)
                current = inte
        ret.append(current)
        return ret