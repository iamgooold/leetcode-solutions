class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp = [[-1]*n for _ in range(n)]
        cnt = [[0]*n for _ in range(n)]
        dp[n-1][n-1], cnt[n-1][n-1] = 0, 1
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) == (n-1, n-1) or board[i][j] == 'X':
                    continue
                best, ways = -1, 0
                for ni, nj in ((i+1,j), (i,j+1), (i+1,j+1)):
                    if ni < n and nj < n and dp[ni][nj] != -1:
                        if dp[ni][nj] > best:
                            best, ways = dp[ni][nj], cnt[ni][nj]
                        elif dp[ni][nj] == best:
                            ways = (ways + cnt[ni][nj]) % MOD
                if best != -1:
                    val = 0 if (i, j) == (0, 0) else int(board[i][j])
                    dp[i][j], cnt[i][j] = best + val, ways
        return [dp[0][0], cnt[0][0]] if dp[0][0] != -1 else [0, 0]