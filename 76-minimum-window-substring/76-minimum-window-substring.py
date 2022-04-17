class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        found = 0
        
        count = Counter(t)
        
        left = 0
        
        res = ''
        
        for right in range(len(s)):
            
            if s[right] in count:
                
                count[s[right]] -= 1
                
                if count[s[right]] >= 0:
                    
                    found += 1
            
            while found == len(t):
                
                if not res or (right-left+1) < len(res):
                    
                    res = s[left:right+1]
                
                if s[left] in count:
                    
                    count[s[left]] += 1
                    
                    if count[s[left]] > 0:
                        found -= 1
                
                left += 1
        
        
        return res
                    
            
            