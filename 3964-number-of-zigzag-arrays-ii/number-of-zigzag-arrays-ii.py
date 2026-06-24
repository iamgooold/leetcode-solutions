import numpy as np

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        
        T = np.zeros((size, size), dtype=np.int64)
        for i in range(m):
            for j in range(m):
                if j < i:
                    T[j*2, i*2+1] = 1
                if j > i:
                    T[j*2+1, i*2] = 1
        
        def mat_mul(A, B):
            SPLIT = 1 << 15
            A1, A2 = A >> 15, A & (SPLIT - 1)
            return ((A1 @ B % MOD) * SPLIT + A2 @ B) % MOD
        
        def mat_pow(M, p):
            result = np.eye(size, dtype=np.int64)
            base = M.copy()
            while p:
                if p & 1:
                    result = mat_mul(result, base)
                base = mat_mul(base, base)
                p >>= 1
            return result
        
        Tn = mat_pow(T, n - 1)
        return int(Tn.sum() % MOD)