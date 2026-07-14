class Solution:
    def prefixCount(self, words, pref):
        return sum(1 for w in words if w.startswith(pref))