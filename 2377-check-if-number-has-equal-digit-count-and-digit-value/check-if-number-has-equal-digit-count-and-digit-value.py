class Solution:
    def digitCount(self, num: str) -> bool:
        return all(num.count(str(i)) == int(d) for i, d in enumerate(num))