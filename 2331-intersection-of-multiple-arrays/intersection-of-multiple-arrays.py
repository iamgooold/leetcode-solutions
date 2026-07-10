class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])
        for arr in nums[1:]:
            result &= set(arr)
        return sorted(result)