class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for r, node in enumerate(order):
            pos[node] = r
        vals = [nums[node] for node in order]
        
        right = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and vals[j+1] - vals[i] <= maxDiff:
                j += 1
            right[i] = j
        
        LOG = max(1, n.bit_length())
        anc = [[0]*n for _ in range(LOG)]
        anc[0] = right[:]
        for k in range(1, LOG):
            for i in range(n):
                anc[k][i] = anc[k-1][anc[k-1][i]]
        
        def minHops(a, b):
            if a == b:
                return 0
            if a > b:
                a, b = b, a
            if right[a] >= b:
                return 1
            cur = a
            hops = 0
            for k in reversed(range(LOG)):
                if anc[k][cur] < b and anc[k][cur] > cur:
                    hops += (1 << k)
                    cur = anc[k][cur]
            if right[cur] >= b:
                return hops + 1
            return -1
        
        res = []
        for u, v in queries:
            res.append(minHops(pos[u], pos[v]))
        return res