class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.n = n
        self.d = 0
        self.ad = 0

    def move(self, row: int, col: int, player: int) -> int:
        
        if player == 1:
            offset = 1
        else:
            offset = -1
        
        self.row[row] += offset
        self.col[col] += offset
        
        if row == col:
            self.d += offset
        
        if col == self.n - row - 1:
            self.ad += offset
        
        if self.n in [self.row[row], self.col[col], self.d, self.ad]:
            return 1
        
        if -self.n in [self.row[row], self.col[col], self.d, self.ad]:
            return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)