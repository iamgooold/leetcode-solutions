class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res += grid[i][j] * 4 + 2 # 4 sides + top/bottom
                    if i > 0: res -= min(grid[i][j], grid[i-1][j]) * 2
                    if j > 0: res -= min(grid[i][j], grid[i][j-1]) * 2
        return res