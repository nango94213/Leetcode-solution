class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        islands = set()
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        m = len(grid)
        n = len(grid[0])
        
        
        def dfs(i, j):
            
            grid[i][j] = 0
            
            island.add((i-row, j-col))
            
            for d in directions:
                
                x = i + d[0]
                y = j + d[1]
                
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)
            
        
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = set()
                
                    row = i
                    col = j
                
                    dfs(i, j)
                
                    islands.add(frozenset(island))
        return len(islands)
                