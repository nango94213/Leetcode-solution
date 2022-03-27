class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1
        
        for y in range(1,n):
            if obstacleGrid[0][y] == 0 and dp[0][y-1] == 1:
                dp[0][y] = 1
        
        for x in range(1,m):
            if obstacleGrid[x][0] == 0 and dp[x-1][0] == 1:
                dp[x][0] = 1
        
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0
                else:
                    dp[x][y] = dp[x][y-1] + dp[x-1][y]
        
        return dp[-1][-1]