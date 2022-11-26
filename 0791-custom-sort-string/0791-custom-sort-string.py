class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        
        res = ''
        
        for o in order:
            res += o * count[o]
            count[o] = 0
        
        for k in count:
            if count[k] > 0:
                res += k * count[k]
        
        return res