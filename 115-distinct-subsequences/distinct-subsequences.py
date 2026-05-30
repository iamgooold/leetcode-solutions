class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [1] + [0] * n

        for i in range(1, m + 1):
            prev = dp[0]
            for j in range(1, n + 1):
                temp = dp[j]
                if s[i - 1] == t[j - 1]:
                    dp[j] += prev
                prev = temp

        return dp[n]