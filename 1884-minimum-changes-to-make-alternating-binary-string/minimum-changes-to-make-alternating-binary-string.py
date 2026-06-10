class Solution:
    def minOperations(self, s: str) -> int:
        cost = sum(int(c) != i % 2 for i, c in enumerate(s))
        return min(cost, len(s) - cost)