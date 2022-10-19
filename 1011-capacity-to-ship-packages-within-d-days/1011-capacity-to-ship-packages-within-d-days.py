class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            day = 1
            current = 0
            
            for w in weights:
                if current + w > mid:
                    day += 1
                    current = w
                    continue
                
                current += w
            
            if day > days:
                left = mid + 1
                continue
            
            right = mid
        
        return left
                