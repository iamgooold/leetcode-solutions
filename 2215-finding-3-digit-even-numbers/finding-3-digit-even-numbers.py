class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = Counter(digits)
        res = []
        for num in range(100, 1000, 2):
            d = [num // 100, (num // 10) % 10, num % 10]
            need = Counter(d)
            if all(cnt[k] >= v for k, v in need.items()):
                res.append(num)
        return res