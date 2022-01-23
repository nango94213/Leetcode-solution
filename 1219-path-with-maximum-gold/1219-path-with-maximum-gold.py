class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i,j,path):
            nonlocal res
            #if grid[i][j]==0:
                #return
            
            path += grid[i][j]
            res = max(path, res)
            
            tmp = grid[i][j]
            grid[i][j]=0
            
            for d in direction:
                new_i = i + d[0]
                new_j = j + d[1]
                
                if 0 <= new_i < len(grid) and 0<= new_j < len(grid[0]) and grid[new_i][new_j]!=0:
                    dfs(new_i, new_j, path)
            grid[i][j] = tmp
      
 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    dfs(i,j, 0)
                    
        
        
        
        
        return res