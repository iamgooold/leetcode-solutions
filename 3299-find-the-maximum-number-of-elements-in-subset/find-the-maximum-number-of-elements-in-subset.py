class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        for x in cnt:
            if x == 1:
                ones = cnt[1]
                ans = max(ans, ones if ones % 2 == 1 else ones - 1)
                continue

            if cnt[x] < 2:
                continue

            cur = x * x
            if cur not in cnt:
                continue

            length = 3
            cur2 = cur * cur

            while cur2 in cnt:
                if cnt[cur] >= 2:
                    length += 2
                    cur = cur2
                    cur2 = cur * cur
                else:
                    break

            ans = max(ans, length)

        return ans