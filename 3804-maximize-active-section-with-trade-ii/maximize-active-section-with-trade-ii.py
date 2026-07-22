class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        lookup = [-1]*n
        idxs = []
        cnt1 = 0
        for i, x in enumerate(s):
            if x == '0':
                if i and s[i-1] == '0':
                    idxs[-1][1] += 1
                else:
                    idxs.append([i, 1])
            else:
                cnt1 += 1
            lookup[i] = len(idxs)-1

        if not idxs:
            return [cnt1]*len(queries)

        m = len(idxs)-1
        arr = [idxs[i][1]+idxs[i+1][1] for i in range(m)]
        sz = 1
        while sz < max(m,1):
            sz <<= 1
        seg = [0]*(2*sz)
        for i, v in enumerate(arr):
            seg[sz+i] = v
        for i in range(sz-1, 0, -1):
            seg[i] = max(seg[2*i], seg[2*i+1])

        def qmax(l, r):
            l += sz; r += sz+1
            res = -1
            while l < r:
                if l & 1:
                    res = max(res, seg[l]); l += 1
                if r & 1:
                    r -= 1; res = max(res, seg[r])
                l >>= 1; r >>= 1
            return res

        result = [cnt1]*len(queries)
        for i, (l, r) in enumerate(queries):
            left, right = lookup[l]+1, lookup[r]-(s[r]=='0')
            left_cnt = idxs[lookup[l]][1]-(l-idxs[lookup[l]][0]) if lookup[l] != -1 else -1
            right_cnt = r-idxs[lookup[r]][0]+1 if lookup[r] != -1 else -1
            if left <= right-1:
                result[i] = max(result[i], cnt1+qmax(left, right-1))
            if s[l] == '0' and s[r] == '0' and lookup[l]+1 == lookup[r]:
                result[i] = max(result[i], cnt1+left_cnt+right_cnt)
            if s[l] == '0' and lookup[l]+1 <= right:
                result[i] = max(result[i], cnt1+left_cnt+idxs[lookup[l]+1][1])
            if s[r] == '0' and left <= lookup[r]-1:
                result[i] = max(result[i], cnt1+right_cnt+idxs[lookup[r]-1][1])
        return result