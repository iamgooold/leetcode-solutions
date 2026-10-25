class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = 0
        m = min(a, b)
        for i in range(1, m + 1):
            if a % i == 0 and b % i == 0:
                g += 1
        return g