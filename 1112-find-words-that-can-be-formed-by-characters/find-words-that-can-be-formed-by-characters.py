class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for w in words:
            if all(count[c] >= w.count(c) for c in set(w)):
                res += len(w)
        return res