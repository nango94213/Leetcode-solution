class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left = 0
        right = x // 2
        
        while left <= right:
            mid = (left+right) // 2
            if mid**2 == x:
                return mid
            
            if mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
        
        