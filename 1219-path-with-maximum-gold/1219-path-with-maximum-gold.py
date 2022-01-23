class Solution:
    def getMaximumGold(self, grid):
        self.ret = 0 # global varible
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dfs(grid, i, j, 0)
        return self.ret

    def dfs(self, grid, i, j, val):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]: # prunning
            tmp = grid[i][j]
            val += grid[i][j]
            grid[i][j] = 0 # act as visited[i][j]
            self.ret = max(self.ret, val)
            self.dfs(grid, i + 1, j, val)
            self.dfs(grid, i - 1, j, val)
            self.dfs(grid, i, j + 1, val)
            self.dfs(grid, i, j - 1, val)
            grid[i][j] = tmp # restore stack 
             # restore stack 