class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        
        def dfs(x, y):
            
            grid[x][y] = '0'
            
            for d in directions:
                newX = x + d[0]
                newY = y + d[1]
                
                if 0 <= newX <len(grid) and 0 <= newY < len(grid[0]) and grid[newX][newY] == '1':
                    dfs(newX, newY)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res