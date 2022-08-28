class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        count = 0
        a = ''
        b = ''
        c = ''
        d = ''
        
        for i in range(len(s1)):
            
            if s1[i] != s2[i]:
                count += 1
                
                if count == 1:
                    a = s1[i]
                    b = s2[i]
                if count == 2:
                    c = s1[i]
                    d = s2[i]
                    
                
            
            if count > 2:
                return False
        
        return a == d and b == c