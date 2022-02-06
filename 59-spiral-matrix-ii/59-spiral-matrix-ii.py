class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0]*n for i in range(n)]
        
        left, right, top, bottom = 0, n - 1, 0, n - 1
        
        current = 1
        
        while current <= n*n:
            
            for i in range(left, right+1):
                
                
                matrix[top][i] = current
                current += 1
                
            
            for i in range(top+1, bottom+1):
                
      
                matrix[i][right] = current
                current += 1
                
            if top != bottom:
                for i in range(right-1, left-1, -1):
          
                    matrix[bottom][i] = current
                    current += 1
                
            
            if left != right:
                for i in range(bottom-1, top, -1):
                   
                    matrix[i][left] = current
                    current += 1
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return matrix
                
        