class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(0,3,9), 5:(), 6:(0,1,7), 7:(2,6),8:(1,3),9:(2,4)}
        
        current = [1] * 10
        
        for _ in range(n-1):
            
            nex = [0] * 10
            
            for k in neighbors:
                for neighbor in neighbors[k]:
                    
                    nex[k] += current[neighbor]
            
            current = nex
   
        
        return sum(current)%(10**9 + 7)
         