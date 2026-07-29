class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        cs, ct = Counter(s), Counter(target)
        return min(cs[c] // v for c, v in ct.items())