class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        prev = 0
        for upper, pct in brackets:
            if income <= prev:
                break
            tax += (min(income, upper) - prev) * pct / 100
            prev = upper
        return tax