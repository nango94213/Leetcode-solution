class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum % 2 != 0:
            return []
        
        res = []
        
        current = 2
        cum_sum = 0
        
        while cum_sum + current <= finalSum:
            
            res.append(current)
            
            cum_sum += current
            
            current += 2
        
        if cum_sum < finalSum:
            
            res[-1] = res[-1] + finalSum - cum_sum
        
        return res
        
        
        