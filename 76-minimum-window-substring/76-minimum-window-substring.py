import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = collections.Counter(t)
        found = 0
        l = 0
        res = ''

        for r in range(len(s)):
            if s[r] in target:
                
                target[s[r]] -= 1
                if target[s[r]] >= 0:
                    found += 1


            while found==len(t):
                if not res or (r-l+1) < len(res):
                    res = s[l:r+1]
                
                if s[l] in target:
                    target[s[l]] += 1
                    if target[s[l]] > 0: 
                        found -= 1
                l += 1
        
        return res
        
        
        