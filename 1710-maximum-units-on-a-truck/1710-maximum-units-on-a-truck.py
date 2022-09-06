class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        res = 0
        
        for b in boxTypes:
            
            if truckSize == 0:
                break
            
            if b[0] <= truckSize:
                res += b[1] * b[0]
                
                truckSize -= b[0]
                continue
            
            res += truckSize * b[1]
            truckSize = 0
        
        return res
            
        