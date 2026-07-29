class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n = len(nums) // 2
            newNums = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    newNums[i] = min(nums[2*i], nums[2*i+1])
                else:
                    newNums[i] = max(nums[2*i], nums[2*i+1])
            nums = newNums
        return nums[0]