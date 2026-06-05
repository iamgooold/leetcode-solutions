class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for x in arr1:
            lo, hi = bisect_left(arr2, x - d), bisect_right(arr2, x + d)
            if lo == hi:
                res += 1
        return res