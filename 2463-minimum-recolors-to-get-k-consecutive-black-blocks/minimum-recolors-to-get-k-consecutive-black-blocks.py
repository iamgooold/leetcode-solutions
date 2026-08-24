class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # count W in first window
        w = blocks[:k].count('W')
        ans = w
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                w -= 1
            if blocks[i] == 'W':
                w += 1
            ans = min(ans, w)
        return ans