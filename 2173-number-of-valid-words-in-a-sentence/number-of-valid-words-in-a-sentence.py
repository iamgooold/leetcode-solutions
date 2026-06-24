class Solution:
    def countValidWords(self, sentence: str) -> int:
        def valid(token):
            hyphens = 0
            for i, c in enumerate(token):
                if c.isdigit():
                    return False
                if c == '-':
                    hyphens += 1
                    if hyphens > 1 or i == 0 or i == len(token)-1 or not token[i-1].isalpha() or not token[i+1].isalpha():
                        return False
                if c in '!.,':
                    if i != len(token) - 1:
                        return False
            return True
        return sum(valid(t) for t in sentence.split())