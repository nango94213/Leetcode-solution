class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        res = 0
       
        for j in range(1, n):
            for i in range(m):
                if j - 1 >= 0 and grid[i][j] > grid[i][j-1] and (dp[i][j-1]>0 or j-1 == 0):
                    dp[i][j] = max(dp[i][j], dp[i][j-1]+1)
                if j - 1 >= 0 and i + 1 < m and grid[i][j] > grid[i+1][j-1] and (dp[i+1][j-1]>0 or j-1 == 0):
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1]+1)
                if j - 1 >= 0 and i - 1 >= 0 and grid[i][j] > grid[i-1][j-1] and (dp[i-1][j-1]>0 or j-1 == 0):
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
                
                res = max(res, dp[i][j])

        return res
                
            
                    
                
        
        
        