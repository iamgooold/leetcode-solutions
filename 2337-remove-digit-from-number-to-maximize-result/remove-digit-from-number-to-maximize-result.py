class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        best = ""
        for i in range(len(number)):
            if number[i] == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > best:
                    best = candidate
        return best