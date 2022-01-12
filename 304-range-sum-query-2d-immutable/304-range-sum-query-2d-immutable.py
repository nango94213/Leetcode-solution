class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        arr = matrix
        ps = [[0] * len(arr[0]) for i in range(len(arr))]
        R = len(arr)
        C = len(arr[0])
        ps[0][0] = arr[0][0]
        for i in range(1, C):
            ps[0][i] = ps[0][i-1] + arr[0][i]
            
        for i in range(1, R):
            ps[i][0] = ps[i-1][0] + arr[i][0]
        
        for i in range(1, R):
            for j in range(1, C):
                ps[i][j] = ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1] + arr[i][j]
        print(ps)
        self.table = ps
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.table[row2][col2] if row2 >=0 and col2 >= 0 else 0
        b = self.table[row1-1][col1-1] if row1-1 >=0 and col1-1 >= 0 else 0
        c = self.table[row2][col1-1] if row2 >=0 and col1-1 >= 0 else 0
        d = self.table[row1-1][col2] if row1-1 >=0 and col2 >= 0 else 0
        return a + b - c - d
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)