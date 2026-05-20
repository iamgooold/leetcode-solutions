class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        return sum(s in j for s in stones)