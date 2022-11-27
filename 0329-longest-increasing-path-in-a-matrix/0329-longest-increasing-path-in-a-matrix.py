class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        directions = [(0, -1),(-1, 0),(0, 1),(1, 0)]
        
        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[x][y]:
                    dp[x][y] = max(dp[x][y], dfs(i,j))
            
            dp[x][y] += 1
            return dp[x][y]
        
        res = -float('inf')
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        
        return res
        
                