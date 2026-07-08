class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, remaining):
            if len(path) == k:
                if remaining == 0:
                    res.append(path[:])
                return
            for num in range(start, 10):
                if num > remaining:
                    break
                path.append(num)
                backtrack(num+1, path, remaining-num)
                path.pop()
        backtrack(1, [], n)
        return res