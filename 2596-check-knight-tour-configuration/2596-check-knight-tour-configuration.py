class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        direction = set([(1, 2), (2, 1), (2, -1), (1, -2),(-1, -2), (-2, -1), (-2, 1), (-1, 2)])
        mapping = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                mapping[grid[i][j]] = (i, j)
        
        seen = set()
        
        count = x = y = 0
        
        while grid[x][y] not in seen:
            seen.add((x, y))
            count += 1
            
            if grid[x][y] + 1 not in mapping:
                break
            nextM = mapping[grid[x][y]+1]
            if (nextM[0]-x, nextM[1]-y) not in direction:
                break
            x, y = mapping[grid[x][y]+1]
     
        return count == len(grid) * len(grid)
            
            
            
            