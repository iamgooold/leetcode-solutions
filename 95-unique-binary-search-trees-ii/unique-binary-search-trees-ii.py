class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                for left in build(start, i - 1):
                    for right in build(i + 1, end):
                        node = TreeNode(i)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res

        return build(1, n)