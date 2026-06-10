class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(x for x, y in points)
        return max(xs[i+1] - xs[i] for i in range(len(xs)-1))