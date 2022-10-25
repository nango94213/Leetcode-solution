class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        
        res = ''
        
        for c in order:
            if count[c] > 0:
                res += count[c]*c
                count[c] = 0
        
        for c in count:
            if count[c] > 0:
                res += count[c]*c
        
        return res