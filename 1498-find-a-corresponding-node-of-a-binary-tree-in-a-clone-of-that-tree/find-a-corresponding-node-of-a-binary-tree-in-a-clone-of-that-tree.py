class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: return None
        if original == target: return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left: return left
        return self.getTargetCopy(original.right, cloned.right, target)