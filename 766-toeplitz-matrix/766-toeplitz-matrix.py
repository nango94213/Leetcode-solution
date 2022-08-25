class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                
                x = i - 1
                y = j - 1
                
                if (x >= 0 and y >= 0) and matrix[x][y] != matrix[i][j]:
                    return False
        
        return True
        