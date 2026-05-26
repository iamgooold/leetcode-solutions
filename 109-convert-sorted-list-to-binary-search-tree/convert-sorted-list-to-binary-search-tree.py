class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def find_size(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        def build(left, right):
            nonlocal head
            if left > right:
                return None
            mid = (left + right) // 2
            left_node = build(left, mid - 1)
            root = TreeNode(head.val)
            head = head.next
            root.left = left_node
            root.right = build(mid + 1, right)
            return root

        size = find_size(head)
        return build(0, size - 1)