class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check(arr, skip):
            prev = -1
            for i, n in enumerate(arr):
                if i == skip:
                    continue
                if n <= prev:
                    return False
                prev = n
            return True

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return check(nums, i) or check(nums, i - 1)
        return True