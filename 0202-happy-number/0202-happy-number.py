class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set([n])
        
        while True:
            total = 0
            while n:
                total += (n % 10) ** 2
                n = n // 10
            n = total
        
            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
        
        