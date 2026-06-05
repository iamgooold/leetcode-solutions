class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(g)) for _, g in groupby(s))