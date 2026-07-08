class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            lo = bisect.bisect_left(products, prefix)
            suggestions = []
            for i in range(lo, min(lo+3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            res.append(suggestions)
        return res