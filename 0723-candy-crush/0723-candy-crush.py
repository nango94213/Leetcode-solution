class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        m = len(board)
        n = len(board[0])
        
        
        
        
        while True:
            remove = set()
            for j in range(n):
                for i in range(m-2):
                    if board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                        remove.update([(i, j), (i+1, j), (i+2, j)])
            
            
            for i in range(m):
                for j in range(n-2):
                    if board[i][j] == board[i][j+1] == board[i][j+2] != 0:
                        remove.update([(i, j), (i, j+1), (i, j+2)])
            
            
            if not remove:
                return board
            
            
            for j in range(n):
                falling = 0
                for i in range(m-1, -1, -1):
                    if (i, j) not in remove:
                        board[m-1-falling][j] = board[i][j]
                        falling += 1
                    
                    
                
                for i in range(m-falling):
                    board[i][j] = 0
                    