class Solution:
    def countTime(self, time: str) -> int:
        ans = 0
        for h in range(24):
            for m in range(60):
                s = f"{h:02d}:{m:02d}"
                ok = True
                for i in range(5):
                    if time[i] != "?" and time[i] != s[i]:
                        ok = False
                        break
                if ok:
                    ans += 1
        return ans