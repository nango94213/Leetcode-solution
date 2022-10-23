class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j == 0 or i == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
                    
                    res = max(res, dp[i][j])
        
        return res**2