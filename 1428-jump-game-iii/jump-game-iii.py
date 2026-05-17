from collections import deque

class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        q = deque([start])
        seen = {start}
        
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            
            for j in (i + arr[i], i - arr[i]):
                if 0 <= j < n and j not in seen:
                    seen.add(j)
                    q.append(j)
        
        return False