class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3:
            month += 12
            year -= 1
        k = year % 100
        j = year // 100
        h = (day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
        return days[(h + 6) % 7]