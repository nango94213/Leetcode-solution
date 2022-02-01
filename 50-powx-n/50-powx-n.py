class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            n = - n
            x = 1/x
        
        def fastpow(current):
            if current == 0:
                return 1.0
            
            half = fastpow(current//2)
            
            if current % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        return fastpow(n)