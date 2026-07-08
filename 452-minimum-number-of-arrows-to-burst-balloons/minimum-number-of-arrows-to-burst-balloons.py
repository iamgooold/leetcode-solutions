class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for x, y in points[1:]:
            if x > end:
                arrows += 1
                end = y
        return arrows