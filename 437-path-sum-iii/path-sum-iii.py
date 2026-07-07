class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, prefix_sums, target):
            if not node:
                return 0
            prefix_sums[node.val] = prefix_sums.get(node.val, 0) + 1
            count = prefix_sums.get(node.val - target, 0) if False else 0
            return count
        
        def solve(node, curr_sum, prefix, target):
            if not node:
                return 0
            curr_sum += node.val
            count = prefix.get(curr_sum - target, 0)
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            count += solve(node.left, curr_sum, prefix, target)
            count += solve(node.right, curr_sum, prefix, target)
            prefix[curr_sum] -= 1
            return count
        
        return solve(root, 0, {0: 1}, targetSum)