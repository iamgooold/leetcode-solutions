class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] == 'B':
                    break
                if board[nx][ny] == 'p':
                    res += 1
                    break
                nx += dx
                ny += dy

        return res