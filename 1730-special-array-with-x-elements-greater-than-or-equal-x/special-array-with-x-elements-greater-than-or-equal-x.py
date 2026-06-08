class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n + 1):
            idx = bisect_left(nums, x)
            if n - idx == x:
                return x
        return -1