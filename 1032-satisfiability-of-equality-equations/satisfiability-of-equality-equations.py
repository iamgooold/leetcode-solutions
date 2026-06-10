class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for eq in equations:
            if eq[1] == '=':
                union(ord(eq[0]) - 97, ord(eq[3]) - 97)

        for eq in equations:
            if eq[1] == '!':
                if find(ord(eq[0]) - 97) == find(ord(eq[3]) - 97):
                    return False

        return True