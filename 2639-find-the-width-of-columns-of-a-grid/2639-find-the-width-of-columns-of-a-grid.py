class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = []
        for j in range(len(grid[0])):
            res.append(max([len(str(grid[i][j])) for i in range(len(grid))]))
  
        return res
            
        