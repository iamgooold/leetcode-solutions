class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        bar = False
        for c in s:
            if c == '|':
                bar = not bar
            elif c == '*' and not bar:
                count += 1
        return count