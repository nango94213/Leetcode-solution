class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        def dfs(x, y):
            nonlocal res
            grid[x][y] = 0
            gg.add((x, y))
            
            for d in directions:
                newX = x + d[0]
                newY = y + d[1]
                
                if 0 <= newX < m and 0 <= newY < n and grid[newX][newY] == 1:
                    dfs(newX, newY)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    gg = set()
                    dfs(i, j)
                    res = max(res, len(gg))
        
        return res