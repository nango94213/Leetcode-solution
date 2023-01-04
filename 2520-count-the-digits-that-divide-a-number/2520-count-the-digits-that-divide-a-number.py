class Solution:
    def countDigits(self, num: int) -> int:
        
        count = 0
        old = str(num)
        
        for c in old:
            if num % int(c) == 0:
                count += 1
        
        return count
        