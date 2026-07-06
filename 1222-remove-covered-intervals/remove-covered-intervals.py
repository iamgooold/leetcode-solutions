class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        end = 0
        for _, e in intervals:
            if e > end:
                count += 1
                end = e
        return count