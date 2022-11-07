class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])        
        while True:
            current = sum([int(i)**2 for i in str(n)])
            if current == 1:
                return True
            n = current
            if n in seen:
                return False
            seen.add(n)
            
            
            
            