class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = number.replace(' ', '').replace('-', '')
        blocks = []
        i = 0
        while len(digits) - i > 4:
            blocks.append(digits[i:i+3])
            i += 3
        rem = digits[i:]
        if len(rem) == 4:
            blocks += [rem[:2], rem[2:]]
        else:
            blocks.append(rem)
        return '-'.join(blocks)