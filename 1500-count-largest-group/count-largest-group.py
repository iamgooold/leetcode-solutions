class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = Counter(sum(int(d) for d in str(i)) for i in range(1, n + 1))
        mx = max(count.values())
        return sum(1 for v in count.values() if v == mx)