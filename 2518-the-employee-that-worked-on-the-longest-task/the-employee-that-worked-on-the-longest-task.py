class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev = 0
        max_time = -1
        ans = 0
        for id, t in logs:
            cur = t - prev
            if cur > max_time or (cur == max_time and id < ans):
                max_time = cur
                ans = id
            prev = t
        return ans