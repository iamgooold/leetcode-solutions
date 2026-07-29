class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        for c in range(ord('Z'), ord('A')-1, -1):
            if chr(c) in letters and chr(c).lower() in letters:
                return chr(c)
        return ""