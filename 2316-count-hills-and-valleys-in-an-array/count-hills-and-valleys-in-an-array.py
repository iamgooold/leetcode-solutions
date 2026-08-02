class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for x in nums[1:]:
            if x != arr[-1]:
                arr.append(x)
        count = 0
        for i in range(1, len(arr) - 1):
            if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
                count += 1
        return count