class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))
        odd = sorted([d for d in digits if int(d) % 2 == 1], reverse=True)
        even = sorted([d for d in digits if int(d) % 2 == 0], reverse=True)
        oi, ei = 0, 0
        result = []
        for d in digits:
            if int(d) % 2 == 1:
                result.append(odd[oi])
                oi += 1
            else:
                result.append(even[ei])
                ei += 1
        return int(''.join(result))