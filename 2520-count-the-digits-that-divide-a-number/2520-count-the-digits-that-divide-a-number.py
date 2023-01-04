class Solution:
    def countDigits(self, num: int) -> int:
        
        count = 0
        old = num
        while num:
            digit = num % 10
            
            if old % digit == 0:
                count += 1
            num //= 10
       
        return count
        