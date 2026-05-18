class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {s: i for i, s in enumerate(list1)}
        min_sum, res = float('inf'), []

        for j, s in enumerate(list2):
            if s in map1:
                idx_sum = j + map1[s]
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    res = [s]
                elif idx_sum == min_sum:
                    res.append(s)
        return res