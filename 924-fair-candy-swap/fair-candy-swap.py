class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumA - sumB) // 2
        setB = set(bobSizes)
        for a in aliceSizes:
            b = a - diff
            if b in setB:
                return [a, b]