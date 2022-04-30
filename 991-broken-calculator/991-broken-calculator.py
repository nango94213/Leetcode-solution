class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        steps = 0
        
        while target > startValue:
            
            steps += 1
            
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        
        return steps + startValue - target

        
        
        