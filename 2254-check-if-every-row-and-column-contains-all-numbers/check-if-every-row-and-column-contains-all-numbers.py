class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        target = set(range(1, n+1))
        for row in matrix:
            if set(row) != target:
                return False
        for col in zip(*matrix):
            if set(col) != target:
                return False
        return True