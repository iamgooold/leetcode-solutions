class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i, h in sorted(enumerate(arr), key=lambda x: x[1]):
            dp[i] = 1
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= h: break
                dp[i] = max(dp[i], dp[j] + 1)
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= h: break
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)