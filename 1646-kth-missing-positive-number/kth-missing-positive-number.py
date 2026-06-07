class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        i = 0
        num = 0
        while i < k:
            num += 1
            if num not in s:
                i += 1
        return num