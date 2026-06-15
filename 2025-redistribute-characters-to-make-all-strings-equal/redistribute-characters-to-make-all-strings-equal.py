class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter("".join(words))
        n = len(words)
        return all(v % n == 0 for v in count.values())