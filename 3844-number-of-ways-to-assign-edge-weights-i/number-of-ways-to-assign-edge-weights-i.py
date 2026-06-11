from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_depth = 0
        q = deque([(1, 0, 0)])
        visited = [False] * (n + 1)
        visited[1] = True
        while q:
            node, parent, depth = q.popleft()
            max_depth = max(max_depth, depth)
            for nb in adj[node]:
                if not visited[nb]:
                    visited[nb] = True
                    q.append((nb, node, depth + 1))

        return pow(2, max_depth - 1, MOD)