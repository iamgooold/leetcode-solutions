class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pref = []
        s = 0
        for x in nums:
            s += x
            pref.append(s)

        import bisect
        ans = []
        for q in queries:
            ans.append(bisect.bisect_right(pref, q))
        return ans