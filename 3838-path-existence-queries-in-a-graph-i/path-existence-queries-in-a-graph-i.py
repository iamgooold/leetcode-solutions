class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        order = sorted(range(n), key=lambda i: nums[i])
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
        
        for i in range(1, n):
            if nums[order[i]] - nums[order[i-1]] <= maxDiff:
                union(order[i], order[i-1])
        
        return [find(u) == find(v) for u, v in queries]