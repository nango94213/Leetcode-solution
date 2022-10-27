class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1/x
        
        def fastPow(n):
            if n == 0:
                return 1.0
            
            half = fastPow(n//2)
            
            if n % 2 == 0:
                return half * half
            return half * half * x
        
        return fastPow(n)