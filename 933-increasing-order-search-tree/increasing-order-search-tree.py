class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        self.cur = dummy
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)
        
        inorder(root)
        return dummy.right