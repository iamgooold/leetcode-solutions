class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for l, r in ranges:
            for i in range(l, r+1):
                covered.add(i)
        return all(i in covered for i in range(left, right+1))