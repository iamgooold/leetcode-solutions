class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        idx = nums.index(m)
        for i, x in enumerate(nums):
            if i!= idx and m < 2 * x:
                return -1
        return idx