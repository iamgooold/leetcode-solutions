class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)
        cnt = [0]*(mx+1)
        for v in nums:
            cnt[v] += 1

        freq = [0]*(mx+1)
        for d in range(1, mx+1):
            total = 0
            for m in range(d, mx+1, d):
                total += cnt[m]
            freq[d] = total*(total-1)//2

        for d in range(mx, 0, -1):
            for m in range(2*d, mx+1, d):
                freq[d] -= freq[m]

        prefix = [0]*(mx+1)
        for d in range(1, mx+1):
            prefix[d] = prefix[d-1] + freq[d]

        import bisect
        result = []
        for q in queries:
            idx = bisect.bisect_right(prefix, q)
            result.append(idx)
        return result