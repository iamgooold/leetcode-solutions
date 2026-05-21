class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if not node:
                return True
            return node.val == val and dfs(node.left, val) and dfs(node.right, val)
        return dfs(root, root.val)