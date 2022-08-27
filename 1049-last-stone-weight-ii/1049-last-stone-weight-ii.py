class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
 
        s = sum(stones)
        
        dp = [0] * (s+1)
        dp[0] = 1
        
        for stone in stones:
            for i in range(s, -1, -1):
                
                if dp[i] == 0 and i - stone >= 0 and dp[i-stone]:
                    dp[i] = 1
            
        
        res = s
        print(dp)
        for psm in range(s+1):
         
            if dp[psm] and (2*psm-s) >= 0:
               
                res = min(res, 2*psm-s)
        
        return res