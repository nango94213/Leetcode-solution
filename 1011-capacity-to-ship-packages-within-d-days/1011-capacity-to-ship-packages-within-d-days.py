class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        
        
        while l < r:
            
            mid = (l + r) // 2
            
            one_ship = weights[0]
            
            day = 1
            
            
            for w in weights[1:]:
                
                if one_ship+w > mid:
                    day += 1
                    
                    one_ship = w
                
                else:
                    one_ship += w
            
            if day > days:
                l = mid + 1
            
            else:
                r = mid
        return l
    
    