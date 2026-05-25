class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        def isPrime(x):
            if x < 2: return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0: return False
            return True
        
        primes = sum(isPrime(i) for i in range(1, n + 1))
        non_primes = n - primes
        res = 1
        for i in range(1, primes + 1):
            res = res * i % MOD
        for i in range(1, non_primes + 1):
            res = res * i % MOD
        return res