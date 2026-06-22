class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cur = sum(c in vowels for c in s[:k])
        res = cur
        for i in range(k, len(s)):
            cur += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(res, cur)
        return res