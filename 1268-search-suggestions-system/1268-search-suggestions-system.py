import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix)
            
            res.append([x for x in products[i:i+3] if x.startswith(prefix)])
        
        return res