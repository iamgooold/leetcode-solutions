class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3!= 0:
            return False

        target = total // 3
        curr_sum = 0
        parts = 0

        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == target:
                parts += 1
                curr_sum = 0
            if parts == 2 and i < len(arr) - 1:
                return True

        return False