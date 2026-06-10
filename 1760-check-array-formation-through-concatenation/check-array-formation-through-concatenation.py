class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            p = d[arr[i]]
            if arr[i:i+len(p)] != p:
                return False
            i += len(p)
        return True