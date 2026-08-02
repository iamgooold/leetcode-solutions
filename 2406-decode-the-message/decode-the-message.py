class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        base = ord('a')
        idx = 0
        for c in key:
            if c == ' ':
                continue
            if c not in mapping:
                mapping[c] = chr(base + idx)
                idx += 1
        return ''.join(' ' if c == ' ' else mapping[c] for c in message)