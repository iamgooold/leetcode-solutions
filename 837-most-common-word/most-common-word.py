class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(w for w in words if w not in banned)
        return max(count, key=count.get)