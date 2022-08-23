class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            time = 0
            
            for p in piles:
                time += math.ceil(p / mid)
            
            if time > h:
                left = mid + 1
            else:
                right = mid
        
        return left
        