class Solution:
    def alternateDigitSum(self, n: int) -> int:
        width = len(str(n))
        res = 0
        current = -1
        
        if width % 2 == 1:
            current = 1
        
        while n:
            res += (n%10) * current
            n //= 10
            current *= -1
        
        return res
        