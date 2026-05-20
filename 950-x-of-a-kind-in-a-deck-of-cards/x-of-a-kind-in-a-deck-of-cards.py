class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        import math
        
        count = Counter(deck)
        g = 0
        for v in count.values():
            g = math.gcd(g, v)
        return g >= 2