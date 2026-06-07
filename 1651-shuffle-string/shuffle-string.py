class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, idx in enumerate(indices):
            res[idx] = s[i]
        return ''.join(res)