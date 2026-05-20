class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = Counter(c.lower() for c in licensePlate if c.isalpha())
        res = ""
        for w in words:
            if not res or len(w) < len(res):
                wc = Counter(w)
                if all(wc[c] >= lp[c] for c in lp):
                    res = w
        return res