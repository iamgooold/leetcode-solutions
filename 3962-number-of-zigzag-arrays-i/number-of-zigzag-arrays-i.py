import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        down = np.ones(m, dtype=np.int64)
        up = np.ones(m, dtype=np.int64)
        for _ in range(n - 1):
            psd = np.empty(m + 1, dtype=np.int64)
            psu = np.empty(m + 1, dtype=np.int64)
            psd[0] = 0; np.cumsum(down, out=psd[1:])
            psu[0] = 0; np.cumsum(up, out=psu[1:])
            psd %= MOD; psu %= MOD
            down = (psu[m] - psu[1:]) % MOD
            up = psd[:-1].copy()
        return int((down.sum() + up.sum()) % MOD)