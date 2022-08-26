class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        allYear = []
        
        for i in logs:
            allYear.append((i[0], True))
            allYear.append((i[1], False))
        
        allYear.sort()
        
        res = allYear[0]
        maxPopulation = 0
        count = 0
        
        for y in allYear:
            
            if y[1]:
                count += 1
            else:
                count -= 1
            
            if count > maxPopulation:
                maxPopulation = count
                res = y[0]
        
        return res