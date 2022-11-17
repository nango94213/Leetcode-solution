class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        if len(nums) % 2 == 0:
            return True
        
        n = len(nums)
        
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = nums[i]
        
        for j in range(1, n):
            for i in range(n-j):
                dp[i][i+j] = max(nums[i]-dp[i+1][i+j], nums[i+j]-dp[i][i+j-1])
        
        if dp[0][-1] >= 0:
            return True
        return False
        
        