class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * (n + 1)
        for i, c in enumerate(s):
            if c.islower():
                lengths[i+1] = lengths[i] + 1
            elif c == '*':
                lengths[i+1] = max(0, lengths[i] - 1)
            elif c == '#':
                lengths[i+1] = lengths[i] * 2
            else:  # '%'
                lengths[i+1] = lengths[i]

        if k >= lengths[n]:
            return '.'

        idx = k
        for i in range(n - 1, -1, -1):
            c = s[i]
            Lprev, Lcur = lengths[i], lengths[i+1]
            if c.islower():
                if idx == Lcur - 1:
                    return c
            elif c == '*':
                pass
            elif c == '#':
                if idx >= Lprev:
                    idx -= Lprev
            else:  # '%'
                idx = Lprev - 1 - idx

        return '.'