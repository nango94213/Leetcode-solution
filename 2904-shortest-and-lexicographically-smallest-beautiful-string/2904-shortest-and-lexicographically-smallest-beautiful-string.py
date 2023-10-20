class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        g = k
        res = float('inf')
        left = 0
        marker = False
        for right in range(len(s)):
            if s[right] == '1':
                k -= 1
            
            while k == 0:
                marker = True
                res = min(res, right-left+1)
                if s[left] == '1':
                    k += 1
                left += 1
            
        
        lowest = s
        left = 0

        for right in range(len(s)):
            if s[right] == '1':
                g -= 1
            
            while g == 0:
                
                if right-left+1 == res:
   
                    if len(lowest) > right - left + 1:
                        lowest = s[left:right+1]
                    else:
                        lowest = min(lowest, s[left:right+1])
                    
                if s[left] == '1':
                    g += 1
                left += 1
        return lowest if marker else ""
        
        