from typing import List
from collections import Counter

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        cnt = Counter(ranks)
        m = max(cnt.values())

        if m >= 3:
            return "Three of a Kind"
        if m == 2:
            return "Pair"
        return "High Card"