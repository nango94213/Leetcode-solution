class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
   
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        
        def dfs(x, y):
            
            grid[x][y] = 0
            area.add((x, y))
            
            for d in directions:
                newX = x + d[0]
                newY = y + d[1]
                
                if 0 <= newX <len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == 1:
                    dfs(newX, newY)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    area = set()
                    dfs(i, j)
                    res = max(res, len(area))
        
        return res
                    
        