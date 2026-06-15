class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        built = ""
        for w in words:
            built += w
            if built == s:
                return True
            if len(built) >= len(s):
                break
        return False