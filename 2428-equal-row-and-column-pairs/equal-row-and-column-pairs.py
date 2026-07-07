class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = Counter(tuple(row) for row in grid)
        cols = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))
        return sum(rows[k] * cols[k] for k in rows)