class Solution:
    def countDistinct(self, s: str) -> int:
        
        t = {}
        
        count = 0
        
        for i in range(len(s)):
            tmp = t
            for j in range(i, len(s)):
                if s[j] not in tmp:
                    
                    tmp[s[j]] = {}
                    count += 1
                
                tmp = tmp[s[j]]
                
        return count