class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        directions = [(0, -1),(-1, 0),(0, 1),(1, 0)]
        
        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            
            for d in directions:
                
                x = i + d[0]
                y = j + d[1]
          
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(x, y))
                    
            
            dp[i][j] += 1
            
            return dp[i][j]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res
                