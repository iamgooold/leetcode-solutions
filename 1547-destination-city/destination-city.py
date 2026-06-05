class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = {p[0] for p in paths}
        return next(p[1] for p in paths if p[1] not in sources)