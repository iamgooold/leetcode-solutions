class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        arr = [grid[i][j] for i in range(m) for j in range(n)]
        arr = arr[-k:] + arr[:-k]
        return [arr[i*n:(i+1)*n] for i in range(m)]