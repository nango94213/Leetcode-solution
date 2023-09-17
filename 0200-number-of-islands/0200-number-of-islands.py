class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        def dfs(x, y):
            
            grid[x][y] = '0'
            
            
            for d in directions:
                newX = x + d[0]
                newY = y + d[1]
                
                if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == '1':
                    dfs(newX, newY)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1 
                    dfs(i, j)
        
        return res