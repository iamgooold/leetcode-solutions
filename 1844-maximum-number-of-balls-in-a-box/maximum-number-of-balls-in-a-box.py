class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        from collections import defaultdict
        boxes = defaultdict(int)
        for n in range(lowLimit, highLimit + 1):
            boxes[sum(int(d) for d in str(n))] += 1
        return max(boxes.values())