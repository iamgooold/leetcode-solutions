from typing import List
from collections import deque

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def count_lt(d):
            if d <= 0:
                return 0
            dqx, dqn = deque(), deque()
            res, l = 0, 0
            for r in range(n):
                while dqx and nums[dqx[-1]] <= nums[r]: dqx.pop()
                dqx.append(r)
                while dqn and nums[dqn[-1]] >= nums[r]: dqn.pop()
                dqn.append(r)
                while nums[dqx[0]] - nums[dqn[0]] >= d:
                    l += 1
                    if dqx[0] < l: dqx.popleft()
                    if dqn[0] < l: dqn.popleft()
                res += r - l + 1
            return res

        def sum_val_lt(d):
            if d <= 0:
                return 0
            # sum of max(l..r) for valid windows using monotonic deque + running sum
            dqx, dqn = deque(), deque()
            l = 0
            res = 0
            # track sum of max and min for windows ending at r with l' in [l..r]
            # use "sum of subarray max" style: each deque entry stores (index, count)
            # where count = number of starting positions for which this element is the max
            sum_mx = 0
            sum_mn = 0
            cnt = 0  # number of valid starting positions = r - l + 1

            for r in range(n):
                v = nums[r]

                # maintain max deque with counts
                mx_add = 1
                while dqx and nums[dqx[-1][0]] <= v:
                    idx, c = dqx.pop()
                    sum_mx -= nums[idx] * c
                    mx_add += c
                dqx.append((r, mx_add))
                sum_mx += v * mx_add

                mn_add = 1
                while dqn and nums[dqn[-1][0]] >= v:
                    idx, c = dqn.pop()
                    sum_mn -= nums[idx] * c
                    mn_add += c
                dqn.append((r, mn_add))
                sum_mn += v * mn_add

                cnt += 1

                # shrink from left while max - min >= d
                while dqx and dqn and nums[dqx[0][0]] - nums[dqn[0][0]] >= d:
                    # remove leftmost starting position
                    cnt -= 1
                    idx_x, c_x = dqx[0]
                    idx_n, c_n = dqn[0]
                    sum_mx -= nums[idx_x]
                    dqx[0] = (idx_x, c_x - 1)
                    if dqx[0][1] == 0:
                        dqx.popleft()

                    sum_mn -= nums[idx_n]
                    dqn[0] = (idx_n, c_n - 1)
                    if dqn[0][1] == 0:
                        dqn.popleft()

                res += sum_mx - sum_mn

            return res

        def total_sum():
            s_max = 0
            stk = []
            for i in range(n):
                while stk and nums[stk[-1]] < nums[i]:
                    j = stk.pop()
                    left = stk[-1] if stk else -1
                    s_max += nums[j] * (j - left) * (i - j)
                stk.append(i)
            while stk:
                j = stk.pop()
                left = stk[-1] if stk else -1
                s_max += nums[j] * (j - left) * (n - j)

            s_min = 0
            stk = []
            for i in range(n):
                while stk and nums[stk[-1]] > nums[i]:
                    j = stk.pop()
                    left = stk[-1] if stk else -1
                    s_min += nums[j] * (j - left) * (i - j)
                stk.append(i)
            while stk:
                j = stk.pop()
                left = stk[-1] if stk else -1
                s_min += nums[j] * (j - left) * (n - j)

            return s_max - s_min

        total_cnt = n * (n + 1) // 2
        lo, hi = 0, max(nums) - min(nums)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if total_cnt - count_lt(mid) >= k:
                lo = mid
            else:
                hi = mid - 1

        D = lo
        gt_cnt = total_cnt - count_lt(D + 1)
        sum_gt = total_sum() - sum_val_lt(D + 1)

        return sum_gt + (k - gt_cnt) * D