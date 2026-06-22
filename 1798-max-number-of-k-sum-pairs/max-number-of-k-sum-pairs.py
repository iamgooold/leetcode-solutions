class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ops = 0
        for n in count:
            complement = k - n
            if complement in count:
                if n == complement:
                    ops += count[n] // 2
                elif n < complement:
                    ops += min(count[n], count[complement])
        return ops