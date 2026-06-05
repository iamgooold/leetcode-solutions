class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        cw = sum(distance[start:destination])
        return min(cw, sum(distance) - cw)