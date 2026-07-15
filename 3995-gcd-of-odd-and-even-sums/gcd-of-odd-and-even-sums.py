class Solution:
    def gcdOfOddEvenSums(self, n):
        odd_sum = n * n
        even_sum = n * (n + 1)
        return __import__("math").gcd(odd_sum, even_sum)