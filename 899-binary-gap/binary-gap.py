class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        res = 0
        last = -1
        for i, ch in enumerate(b):
            if ch == '1':
                if last!= -1:
                    res = max(res, i - last)
                last = i
        return res