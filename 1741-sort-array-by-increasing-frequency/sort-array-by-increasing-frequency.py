class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))