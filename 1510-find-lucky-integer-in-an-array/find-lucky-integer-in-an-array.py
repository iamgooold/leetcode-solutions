class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        return max((k for k, v in count.items() if k == v), default=-1)