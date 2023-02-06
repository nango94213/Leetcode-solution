class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        dp = [0] * (len(prizePositions)+1)
        
        left = 0
        res = 0
        for right in range(len(prizePositions)):
            while prizePositions[left] + k < prizePositions[right]:
                left += 1
            dp[right+1] = max(dp[right], right-left+1)
            
            res = max(res, right-left+1+dp[left])
        return res