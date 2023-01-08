class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left = 1
        right = max(candies)
        
        while left < right:
            mid = (left+right+1) // 2
            
            count = 0
            
            for c in  candies:
                count += (c // mid)
            
            if count < k:
                right = mid - 1
            else:
                left = mid
        
        return left
        