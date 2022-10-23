class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        m = len(board)
        n = len(board[0])
        
        bound = set()
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i in (0, m-1) or j in (0, n-1)):
                    bound.add((i, j))
        
        
        def dfs(x, y):
            board[x][y] = '#'
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                    dfs(i, j)
        
        for i, j in bound:
            dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
        return board