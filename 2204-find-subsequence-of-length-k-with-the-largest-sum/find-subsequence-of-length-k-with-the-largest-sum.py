class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        idx = sorted(range(len(nums)), key=lambda i: -nums[i])[:k]
        idx.sort()
        return [nums[i] for i in idx]