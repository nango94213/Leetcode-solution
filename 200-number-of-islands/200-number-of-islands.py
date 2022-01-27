class Solution(object):
    def numIslands(self, grid):
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i,j):
    
            grid[i][j]='0'
            for d in direction:
                new_i = i + d[0]
                new_j = j + d[1]
                
                if 0 <= new_i < len(grid) and 0<= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
                    
        
        
        
        
        return count
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        :type grid: List[List[str]]
        :rtype: int
        
        class Solution(object):
    def numIslands(self, grid):
     
        if grid==None or len(grid)==0:
            return 0
        grid=grid
        self.r=len(grid)
        self.c=len(grid[0])
        count=0
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(i,j,grid)
        return count
                    
    def dfs(self,i,j,grid):
        if i<0 or j<0  or i>=self.r or j>=self.c or grid[i][j]=='0':
            return
        grid[i][j]='0'
        self.dfs(i-1,j,grid)
        self.dfs(i+1,j,grid)
        self.dfs(i,j-1,grid)
        self.dfs(i,j+1,grid)
        """
        