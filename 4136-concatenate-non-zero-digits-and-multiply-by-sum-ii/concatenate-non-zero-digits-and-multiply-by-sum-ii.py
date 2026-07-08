class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        V = [0] * (m + 1)
        C = [0] * (m + 1)
        S = [0] * (m + 1)
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = pow10[i-1] * 10 % MOD
        for i in range(1, m + 1):
            d = int(s[i-1])
            if d != 0:
                V[i] = (V[i-1] * 10 + d) % MOD
                C[i] = C[i-1] + 1
            else:
                V[i] = V[i-1]
                C[i] = C[i-1]
            S[i] = (S[i-1] + d) % MOD
        
        res = []
        for l, r in queries:
            x = (V[r+1] - V[l] * pow10[C[r+1] - C[l]]) % MOD
            total = (S[r+1] - S[l]) % MOD
            res.append((x * total) % MOD)
        return res