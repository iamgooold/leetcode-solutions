class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        col = [0] * n
        for r, c in indices:
            row[r] ^= 1
            col[c] ^= 1
        return sum(row[i] ^ col[j] for i in range(m) for j in range(n))