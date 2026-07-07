class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return count + dfs(node.left, max_val) + dfs(node.right, max_val)
        return dfs(root, root.val)