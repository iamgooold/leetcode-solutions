class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.res = float('inf')
        
        def dfs(node):
            if not node: return
            dfs(node.left)
            if self.prev is not None:
                self.res = min(self.res, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)
        
        dfs(root)
        return self.res