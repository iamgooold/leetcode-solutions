class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for n in nums:
            if k < 2 or nums[k - 2] != n:
                nums[k] = n
                k += 1
        return k