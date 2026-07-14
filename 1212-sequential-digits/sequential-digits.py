class Solution:
    def sequentialDigits(self, low, high):
        digits = "123456789"
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(0, 9 - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
        return sorted(result)