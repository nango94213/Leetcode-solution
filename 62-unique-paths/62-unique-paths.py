class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        '''grid = [[0]*n for _ in range(m)]
   
        
        directions = [(1, 0), (0, 1)]
        
        count = 0
        def dfs(x, y):
            nonlocal count
            grid[x][y] = 1
            
            if x == m-1 and y == n-1:
               
                count += 1
                
            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    dfs(new_x, new_y)
            
            grid[x][y] = 0
        
        dfs(0, 0)
        
        return count'''
        
        dp = [[1]*n for _ in range(m)]
        
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x][y-1] + dp[x-1][y]
        
        return dp[-1][-1]
            
        
        