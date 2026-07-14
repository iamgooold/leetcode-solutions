from math import gcd
from functools import lru_cache

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0
            x = nums[i]
            res = dp(i + 1, gcd(g1, x), g2)
            res += dp(i + 1, g1, gcd(g2, x))
            res += dp(i + 1, g1, g2)
            return res % MOD

        return dp(0, 0, 0)