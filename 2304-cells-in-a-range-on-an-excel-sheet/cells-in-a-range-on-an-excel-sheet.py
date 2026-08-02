class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, c2, r2 = s[0], int(s[1]), s[3], int(s[4])
        return [chr(c) + str(r) for c in range(ord(c1), ord(c2) + 1) for r in range(r1, r2 + 1)]