class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank = {sorted_score[i]: str(i + 1) for i in range(len(score))}
        if len(score) >= 1: rank[sorted_score[0]] = "Gold Medal"
        if len(score) >= 2: rank[sorted_score[1]] = "Silver Medal"
        if len(score) >= 3: rank[sorted_score[2]] = "Bronze Medal"
        return [rank[s] for s in score]