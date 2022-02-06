import collections
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands=set()
        def dfs(i,j):
            
            grid[i][j]=0
            island.add((i-row,j-col))
            
            for d in direction:
                new_x, new_y = i + d[0], j + d[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 0:
                    dfs(new_x, new_y)
  
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    row=i
                    col=j
                    island=set()
                    dfs(i,j)
                    islands.add(frozenset(island))
        return len(islands)