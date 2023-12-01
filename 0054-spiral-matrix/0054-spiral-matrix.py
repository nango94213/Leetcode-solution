class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        total = len(matrix) * len(matrix[0])
        
        while len(res) < total:
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
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return res