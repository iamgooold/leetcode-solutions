class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[''] * 3 for _ in range(3)]
        for i, (r, c) in enumerate(moves):
            grid[r][c] = 'A' if i % 2 == 0 else 'B'

        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2]!= '':
                return grid[i][0]
            if grid[0][i] == grid[1][i] == grid[2][i]!= '':
                return grid[0][i]

        if grid[0][0] == grid[1][1] == grid[2][2]!= '':
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0]!= '':
            return grid[0][2]

        return "Draw" if len(moves) == 9 else "Pending"