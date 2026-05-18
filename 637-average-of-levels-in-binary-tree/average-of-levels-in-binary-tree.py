from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        q, res = deque([root]), []

        while q:
            level_sum = 0
            level_count = len(q)
            for _ in range(level_count):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_sum / level_count)
        return res