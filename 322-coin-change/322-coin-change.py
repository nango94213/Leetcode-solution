class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [float('inf')] * (amount+1)
        
        dp[0] = 0
        
        for m in range(amount+1):
            for c in coins:
                
                if m - c >= 0:
                    dp[m] = min(dp[m], dp[m-c]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
            
        
        
        
        
        