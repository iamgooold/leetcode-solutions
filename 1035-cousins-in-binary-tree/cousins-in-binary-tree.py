# Definition for a binary tree node.
# class TreeNode:
# def __init__(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = collections.deque([(root, None)])

        while q:
            size = len(q)
            parents = {}
            for _ in range(size):
                node, parent = q.popleft()
                if node.val == x:
                    parents[x] = parent
                if node.val == y:
                    parents[y] = parent
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            if x in parents and y in parents:
                return parents[x]!= parents[y]
            if x in parents or y in parents:
                return False

        return False