class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        
        dp = [False] * (target+1)
        dp[0] = True
        
        
        for n in nums:
            for i in range(target, 0, -1):
                if i >= n:
                    dp[i] = dp[i] or dp[i-n]
        
        return dp[-1]