class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        directions = [(1, 0), (0, 1)]
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0]*(cols) for i in range(rows)]

        def dfs(x, y):
            
            if dp[x][y]!= 0:
                return dp[x][y]
            
            tmp = float('inf')
            
            for d in directions:
                
                newx = x + d[0]
                newy = y + d[1]
                
                
                if 0 <= newx < rows and 0 <= newy < cols:
                    tmp = min(tmp, dfs(newx, newy))
                    
            if tmp  == float('inf'):
                tmp = 0
                
            dp[x][y] += (grid[x][y] + tmp)
            
            return dp[x][y]
        
        dfs(0, 0)
        
        return dp[0][0]
                
        
      

        