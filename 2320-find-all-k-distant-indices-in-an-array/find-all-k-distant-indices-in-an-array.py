class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        keyIndices = [i for i, v in enumerate(nums) if v == key]
        result = []
        for i in range(n):
            if any(abs(i - j) <= k for j in keyIndices):
                result.append(i)
        return result