class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for i in range(m)]
        direction = [(0, -1),(-1, 0),(0, 1),(1, 0)]
        def dfs(i,j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            for d in direction:
                new_i = i + d[0]
                new_j = j + d[1]
                
                if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(new_i, new_j))
            
            dp[i][j] += 1
            
            return dp[i][j]
            
                
        
        res = 0
        for x in range(m):
            for y in range(n):
                res = max(res, dfs(x, y))
                
        return res