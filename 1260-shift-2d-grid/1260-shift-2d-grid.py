class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        for _ in range(k):
            
            for i in range(1, len(grid)):
                last = grid[i-1].pop()
                grid[i].insert(0, last)
            
            last = grid[-1].pop()
            grid[0].insert(0, last)
        
        return grid
            