class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {0: 1}
        res = 0
        
        current = 0
        
        for n in nums:
            current += n
            if current-k in dp:
                res += dp[current-k]
            
            dp[current] = 1 if current not in dp else dp[current] + 1
        
        return res
        