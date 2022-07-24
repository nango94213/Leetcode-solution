class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        
        for r in range(0, query_row+1):
            for g in range(0, r+1):
                
                excess = (A[r][g] - 1.0) / 2.0
  
                if excess > 0:
                    A[r+1][g] += excess
                    A[r+1][g+1] += excess
        
        return min(1, A[query_row][query_glass])
                
                