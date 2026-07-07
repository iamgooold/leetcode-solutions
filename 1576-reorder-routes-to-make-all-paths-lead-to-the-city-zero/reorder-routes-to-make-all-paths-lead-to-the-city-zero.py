class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))
        
        visited = [False] * n
        stack = [0]
        visited[0] = True
        count = 0
        while stack:
            node = stack.pop()
            for neighbor, cost in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += cost
                    stack.append(neighbor)
        return count