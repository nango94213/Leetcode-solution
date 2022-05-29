class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        res = []
    
        
        for i in range(len(logs)):
            
            res.append((logs[i][0], True))
            res.append((logs[i][1], False))

        
        res.sort()
        
        count = 0
        final = 0
        year = 0
   
        for i in res:
            
            if i[1]:
                count += 1
            else:
                count -= 1
            
            if count > final:
                year = i[0]
                final = count
        
        return year
            
            