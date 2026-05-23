class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        idx = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[idx] = nums[left] * nums[left]
                left += 1
            else:
                res[idx] = nums[right] * nums[right]
                right -= 1
            idx -= 1

        return res