class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        
        pre_two = 1
        pre_one = 1
        
        if n == 1:
            return 1
        
        for i in range(2, n+1):
            current = pre_two + pre_one
            
            pre_one, pre_two = current, pre_one
        
        return pre_one
        