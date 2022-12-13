class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        res = 0
        
        for s in strs:
            if s.isdigit():
                res = max(res, int(s))
            else:
                res = max(res, len(s))
        return res
    