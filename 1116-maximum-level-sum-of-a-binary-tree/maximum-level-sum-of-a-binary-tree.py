class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque([root])
        level = 0
        max_sum = float('-inf')
        max_level = 0
        while queue:
            level += 1
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if total > max_sum:
                max_sum = total
                max_level = level
        return max_level