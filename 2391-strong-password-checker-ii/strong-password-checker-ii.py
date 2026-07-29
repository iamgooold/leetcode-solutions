class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        special = "!@#$%^&*()-+"
        has_lower = has_upper = has_digit = has_special = False
        for i, c in enumerate(password):
            if i > 0 and c == password[i-1]:
                return False
            if c.islower(): has_lower = True
            elif c.isupper(): has_upper = True
            elif c.isdigit(): has_digit = True
            elif c in special: has_special = True
        return has_lower and has_upper and has_digit and has_special