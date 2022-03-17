class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        row_n=len(board)
        col_n=len(board[0])
        
        def dfs(i,j):
        
            
            count=0
            
            for d in direction:
                x=i+d[0]
                y=j+d[1]
                
                if 0<=x<row_n and 0<=y<col_n and board[x][y]=='M':
                    count+=1
            
            if count:
                board[i][j]=str(count)
                return
            
            board[i][j]='B'
            
            for d in direction:
                x=i+d[0]
                y=j+d[1]
                if 0<=x<row_n and 0<=y<col_n and board[x][y]=='E':
                     dfs(x,y)
                        
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        
        dfs(click[0],click[1])
        
        return board
                
                
                
        