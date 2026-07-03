class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = defaultdict(list)
        for u, v, cost in edges:
            adj[u].append((v, cost))
        
        def feasible(mid):
            if not online[0] or not online[n-1]:
                return False
            dist = [float('inf')] * n
            dist[0] = 0
            indeg = [0]*n
            for u, v, cost in edges:
                if cost >= mid:
                    indeg[v] += 1
            order = []
            temp_indeg = indeg[:]
            q = deque([i for i in range(n) if temp_indeg[i] == 0])
            while q:
                u = q.popleft()
                order.append(u)
                for v, cost in adj[u]:
                    if cost >= mid:
                        temp_indeg[v] -= 1
                        if temp_indeg[v] == 0:
                            q.append(v)
            for u in order:
                if dist[u] == float('inf') or not online[u]:
                    continue
                for v, cost in adj[u]:
                    if cost >= mid and online[v]:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
            return dist[n-1] <= k
        
        lo, hi = 0, max((c for _,_,c in edges), default=0)
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if feasible(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans