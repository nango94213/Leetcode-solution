class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        bound = set()
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            if board[i][0] == 'O':
                bound.add((i, 0))
            if board[i][n-1] == 'O':
                bound.add((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                bound.add((0, j))
            if board[m-1][j] == 'O':
                bound.add((m-1, j))
        
        def dfs(x, y):
            board[x][y] = '#'
            
            for d in directions:
                i = x + d[0]
                j = y + d[1]
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                    dfs(i, j)
        for b in bound:
            dfs(b[0], b[1])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        return board