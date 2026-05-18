from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: return 0

        indices = defaultdict(list)
        for i, v in enumerate(arr):
            indices[v].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1: return steps

                for j in [i - 1, i + 1]:
                    if 0 <= j < n and j not in visited:
                        visited.add(j)
                        q.append(j)

                if arr[i] in indices:
                    for j in indices[arr[i]]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
                    del indices[arr[i]] # avoid TLE

            steps += 1

        return -1