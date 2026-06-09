class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        day = 0
        for i in range(n):
            if i % 7 == 0:
                week += 1
                day = week
            else:
                day += 1
            total += day
        return total