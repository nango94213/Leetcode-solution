class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        
        while True:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            
            if left != right:
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
            if len(res) == m*n:
                break
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return res
        