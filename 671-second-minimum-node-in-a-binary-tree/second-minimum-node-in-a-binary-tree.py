class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        min_val = root.val

        def dfs(node):
            if not node:
                return
            if min_val < node.val < self.ans:
                self.ans = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1