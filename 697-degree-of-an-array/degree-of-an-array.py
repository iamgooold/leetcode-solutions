class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        count = {}
        res = len(nums)
        degree = 0
        
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            count[x] = count.get(x, 0) + 1
            if count[x] > degree:
                degree = count[x]
                res = i - first[x] + 1
            elif count[x] == degree:
                res = min(res, i - first[x] + 1)
        return res