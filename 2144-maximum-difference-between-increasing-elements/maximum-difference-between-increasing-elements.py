class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val, res = nums[0], -1
        for n in nums[1:]:
            if n > min_val:
                res = max(res, n - min_val)
            else:
                min_val = n
        return res