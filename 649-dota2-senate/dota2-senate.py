class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque(i for i, c in enumerate(senate) if c == 'R')
        dire = deque(i for i, c in enumerate(senate) if c == 'D')
        n = len(senate)
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"