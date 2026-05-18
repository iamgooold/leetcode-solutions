class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and isSame(s.left, t.left) and isSame(s.right, t.right)

        if not root: return False
        if isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)