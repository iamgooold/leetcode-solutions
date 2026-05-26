class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)

        return not root or check(root.left, root.right)