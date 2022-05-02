class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        #print(chr(97))
        
        res = ''
        
        while n > 0:
            n -= 1
            
            candidate = k - n
            
            if candidate > 26:
                candidate = 26

            res = chr(96+candidate) + res
            
            k -= candidate
        
        return res