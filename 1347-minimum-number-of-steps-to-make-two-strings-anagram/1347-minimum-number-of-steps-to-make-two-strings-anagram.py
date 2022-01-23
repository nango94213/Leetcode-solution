class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        
        res = 0
        
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                res += 1
        return res
        