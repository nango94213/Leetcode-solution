class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m = len(mat1)
        n = len(mat2[0])
        
        k = len(mat1[0])
        
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                
                for p in range(k):
                    
                    ans[i][j] += mat1[i][p] * mat2[p][j]
        
        return ans
                
                
        