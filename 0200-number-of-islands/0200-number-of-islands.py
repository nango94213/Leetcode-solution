class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = "0"
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res