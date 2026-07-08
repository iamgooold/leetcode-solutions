class SmallestInfiniteSet:
    def __init__(self):
        self.heap = list(range(1, 1001))
        heapq.heapify(self.heap)
        self.in_set = set(self.heap)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.in_set.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.in_set:
            self.in_set.add(num)
            heapq.heappush(self.heap, num)