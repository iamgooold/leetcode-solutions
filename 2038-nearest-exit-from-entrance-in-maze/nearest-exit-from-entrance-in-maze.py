class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        er, ec = entrance
        visited = [[False]*n for _ in range(m)]
        visited[er][ec] = True
        queue = deque([(er, ec, 0)])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r, c, d = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] == '.':
                    if nr == 0 or nr == m-1 or nc == 0 or nc == n-1:
                        return d + 1
                    visited[nr][nc] = True
                    queue.append((nr, nc, d+1))
        return -1