class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        k = len(t)
        
        count = Counter(t)
        
        left = 0
        res = ''
        
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] -= 1
                if count[s[right]] >= 0:
                    k -= 1
            
            while k == 0:
                if not res or len(res) > right - left + 1:
                    res = s[left:right+1]
             
                if s[left] in count:
                    count[s[left]] += 1
                    
                    if count[s[left]] > 0:
                        k += 1
                
                left += 1
        
        return res