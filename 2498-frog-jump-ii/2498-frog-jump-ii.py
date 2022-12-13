class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones) == 2:
            return stones[-1]
        
        res = stones[1]
        
        for i in range(2, len(stones)):
            res = max(res, stones[i]-stones[i-2])
            
        return res
            