class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        MOD = 10**9 + 7

        def count(x):
            if x < 100: return 0
            s = str(x)
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos, tight, pre, prepre, lead, peaks):
                if pos == len(s):
                    return peaks
                res = 0
                up = int(s[pos]) if tight else 9
                for d in range(up + 1):
                    nxt_tight = tight and d == up
                    if lead:
                        if d == 0:
                            res = (res + dfs(pos + 1, nxt_tight, -1, -1, True, peaks)) % MOD
                        else:
                            res = (res + dfs(pos + 1, nxt_tight, d, -1, False, peaks)) % MOD
                    else:
                        new_peaks = peaks
                        if prepre!= -1:
                            if pre > prepre and pre > d: new_peaks += 1
                            elif pre < prepre and pre < d: new_peaks += 1
                        res = (res + dfs(pos + 1, nxt_tight, d, pre, False, new_peaks)) % MOD
                return res

            return dfs(0, True, -1, -1, True, 0)

        return (count(num2) - count(num1 - 1)) % MOD