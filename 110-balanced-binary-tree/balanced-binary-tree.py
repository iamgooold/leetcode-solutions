class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0, True
            left_h, left_bal = check(node.left)
            right_h, right_bal = check(node.right)
            balanced = left_bal and right_bal and abs(left_h - right_h) <= 1
            return 1 + max(left_h, right_h), balanced

        return check(root)[1]