from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                mx = 0
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if grid[r][c] > mx:
                            mx = grid[r][c]
                res[i][j] = mx
        return res