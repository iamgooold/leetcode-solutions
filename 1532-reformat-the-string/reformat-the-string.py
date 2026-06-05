class Solution:
    def reformat(self, s: str) -> str:
        digits = [c for c in s if c.isdigit()]
        letters = [c for c in s if c.isalpha()]
        if abs(len(digits) - len(letters)) > 1:
            return ""
        if len(letters) > len(digits):
            digits, letters = letters, digits
        return ''.join(a + b for a, b in zip_longest(digits, letters, fillvalue=''))