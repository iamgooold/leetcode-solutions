class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            else:
                d = i - first[c] - 1
                if d!= distance[ord(c) - 97]:
                    return False
        return True