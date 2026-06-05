class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total, curr = sum(nums), 0
        for i, n in enumerate(nums):
            curr += n
            if curr > total - curr:
                return nums[:i+1]