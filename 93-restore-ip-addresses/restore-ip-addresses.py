class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(start, path):
            if len(path) == 4:
                if start == n:
                    res.append('.'.join(path))
                return
            for l in range(1, 4):
                if start + l > n:
                    break
                seg = s[start:start + l]
                if (seg[0] == '0' and len(seg) > 1) or int(seg) > 255:
                    continue
                backtrack(start + l, path + [seg])

        backtrack(0, [])
        return res