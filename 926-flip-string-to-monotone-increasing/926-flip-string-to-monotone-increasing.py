class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        res = float('inf')
        
        count0 = s.count('0')
        count1 = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                count0 -= 1
            
            if s[i] == '1':
                
                res = min(res, count1 + count0)
                
                count1 += 1
        
        return min(res, count1 + count0)