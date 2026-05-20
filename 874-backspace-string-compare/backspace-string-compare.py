class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_char(string, idx):
            skip = 0
            while idx >= 0:
                if string[idx] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                idx -= 1
            return idx
        
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = next_valid_char(s, i)
            j = next_valid_char(t, j)
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0 or s[i]!= t[j]:
                return False
            i -= 1
            j -= 1
        return True