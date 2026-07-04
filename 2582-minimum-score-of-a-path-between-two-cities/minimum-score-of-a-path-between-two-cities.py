class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, d in roads:
            adj[u].append((v, d))
            adj[v].append((u, d))
        
        visited = [False] * (n + 1)
        stack = [1]
        visited[1] = True
        ans = float('inf')
        while stack:
            u = stack.pop()
            for v, d in adj[u]:
                ans = min(ans, d)
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return ans