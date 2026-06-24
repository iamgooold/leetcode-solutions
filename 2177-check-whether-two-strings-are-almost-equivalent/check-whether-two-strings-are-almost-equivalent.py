class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c = Counter(word1)
        for ch in word2:
            c[ch] -= 1
        return all(abs(v) <= 3 for v in c.values())