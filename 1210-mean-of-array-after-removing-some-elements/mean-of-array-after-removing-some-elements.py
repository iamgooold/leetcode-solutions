class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr) // 20
        return sum(arr[n:-n]) / len(arr[n:-n])