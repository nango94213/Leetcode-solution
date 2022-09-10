class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        high = [0]
        low = [0]
        
        count = 0 
        
        for i in range(1, len(security)):
            
            if security[i] <= security[i-1]:
                count += 1
            else:
                count = 0
                
                
            high.append(count)
            
        
        count = 0
        for i in range(len(security)-2, -1, -1):
            
            if security[i] <= security[i+1]:
                count += 1
            else:
                count = 0
            low.append(count)
      
            
        low.reverse()
        
        res = []    
        for i, v in enumerate(security):
            if high[i] >= time and low[i] >= time:
                res.append(i)
              
        return res
        
        