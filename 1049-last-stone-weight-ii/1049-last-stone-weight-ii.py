class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        
        dp = [[0] * (s+1) for _ in range(len(stones)+1)]
        
        for i in range(len(stones)+1):
            dp[i][0] = 1
        

        for i in range(1, s+1):
            for j in range(1, len(stones)+1):
                
                if i - stones[j-1] >= 0:
                    if dp[j-1][i] or dp[j-1][i-stones[j-1]]:
                        dp[j][i] = 1
                else:
                    dp[j][i] = dp[j-1][i]

        
        res = s
        
        for psm in range(1, s+1):
            
            if dp[len(stones)][psm] and 2*psm - s >= 0:
                res = min(res, 2*psm-s)
        
        return res
   