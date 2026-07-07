class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_len = 0
        def dfs(node, left_len, right_len):
            if not node:
                return
            self.max_len = max(self.max_len, left_len, right_len)
            dfs(node.left, right_len + 1, 0)
            dfs(node.right, 0, left_len + 1)
        dfs(root, 0, 0)
        return self.max_len