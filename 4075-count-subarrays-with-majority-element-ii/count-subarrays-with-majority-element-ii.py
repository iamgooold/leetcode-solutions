class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n
        size = 2 * n + 2
        bit = [0] * (size + 1)

        def update(i):
            i += 1
            while i <= size:
                bit[i] += 1
                i += i & (-i)

        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        count = 0
        prefix = 0
        update(offset)
        for x in nums:
            prefix += 1 if x == target else -1
            if prefix - 1 + offset >= 0:
                count += query(prefix - 1 + offset)
            update(prefix + offset)
        return count