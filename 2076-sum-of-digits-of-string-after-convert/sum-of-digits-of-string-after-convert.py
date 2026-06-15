class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = "".join(str(ord(c) - 96) for c in s)
        result = sum(int(d) for d in num)
        for _ in range(k - 1):
            result = sum(int(d) for d in str(result))
        return result