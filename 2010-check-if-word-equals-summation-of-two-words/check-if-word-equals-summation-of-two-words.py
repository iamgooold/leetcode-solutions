class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def val(w):
            return int("".join(str(ord(c) - ord('a')) for c in w))
        return val(firstWord) + val(secondWord) == val(targetWord)