class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        
        res = 0
        
        def dfs(x, y, path):
            nonlocal res
            gold = grid[x][y]
            path += gold
            
            res = max(res, path)
            
            grid[x][y] = 0
            
            for d in direction:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n and grid[i][j] != 0:
                    dfs(i, j, path)
                    
            grid[x][y] = gold
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)
        
        return res
            