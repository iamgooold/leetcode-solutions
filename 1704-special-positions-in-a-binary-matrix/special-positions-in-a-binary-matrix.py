class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(
            mat[r][c] == 1 and sum(mat[r]) == 1 and sum(mat[i][c] for i in range(len(mat))) == 1
            for r in range(len(mat)) for c in range(len(mat[0]))
        )