class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(t) < len(s):
            return False
        a = 0
        b = 0
        
        while a < len(s):
            if b >= len(t):
                    return False
            if s[a] == t[b]:
                a += 1
                b += 1
            else:
                b += 1
            
        return True