class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, cur = 1, 0
        for c in s:
            w = widths[ord(c) - 97]
            if cur + w > 100:
                lines += 1
                cur = w
            else:
                cur += w
        return [lines, cur]