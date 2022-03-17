class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        row_n=len(board)
        col_n=len(board[0])
        
        def dfs(x, y):
            
            count = 0
            for d in direction:
                
                new_x = x + d[0]
                new_y = y + d[1]
                
                if 0 <= new_x < row_n and 0 <= new_y < col_n and board[new_x][new_y] == 'M':
                    count += 1
            
            if count:
                board[x][y] = str(count)
                return 
            
            board[x][y] = 'B'
            for d in direction:
                
                new_x = x + d[0]
                new_y = y + d[1]
                
                if 0 <= new_x < row_n and 0 <= new_y < col_n and board[new_x][new_y] == 'E':
                    dfs(new_x, new_y)
        
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        if board[click[0]][click[1]] == 'E':
            dfs(click[0], click[1])
        
        return board