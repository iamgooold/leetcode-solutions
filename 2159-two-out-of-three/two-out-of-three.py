class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c = Counter()
        for s in [set(nums1), set(nums2), set(nums3)]:
            c.update(s)
        return [k for k, v in c.items() if v >= 2]