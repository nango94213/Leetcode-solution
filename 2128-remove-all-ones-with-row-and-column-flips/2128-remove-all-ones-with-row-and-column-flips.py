class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        
        first_row = grid[0]
        
        for i in range(1, len(grid)):
            
            if grid[i] != first_row and [1-n for n in grid[i]]!= first_row: 
                return False
        
        return True