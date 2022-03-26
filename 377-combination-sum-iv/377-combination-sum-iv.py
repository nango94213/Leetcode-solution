class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        
        for comb_sum in range(target+1):
            
            for n in nums:
                
                if comb_sum - n >= 0:
                    dp[comb_sum] += dp[comb_sum-n]
        
        return dp[-1]