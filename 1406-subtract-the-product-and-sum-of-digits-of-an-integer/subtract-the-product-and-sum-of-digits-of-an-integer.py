class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, total = 1, 0
        while n:
            d = n % 10
            prod *= d
            total += d
            n //= 10
        return prod - total