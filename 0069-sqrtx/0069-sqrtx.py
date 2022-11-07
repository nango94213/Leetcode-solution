class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left = 0
        right = x // 2
        
        while left <= right:
            mid = (left+right) // 2
            
            two = mid * mid
            
            if two == x:
                return mid
            
            if two > x:
                right = mid - 1
            
            if two < x:
                left = mid + 1
        return right
        