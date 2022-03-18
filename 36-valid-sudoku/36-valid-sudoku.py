class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
            
        row_tracker = [set() for _ in range(n)]
        col_tracker = [set() for _ in range(n)]
        box_tracker = [set() for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                
                value = board[i][j]
                
                if value == '.':
                    continue
                
                if value in row_tracker[i]:
                    return False
                
                row_tracker[i].add(value)
                
                if value in col_tracker[j]:
                    return False
                
                col_tracker[j].add(value)
                
                if value in box_tracker[(i//3)*3+(j//3)]:
                    return False
                
                box_tracker[(i//3)*3+(j//3)].add(value)
        
        return True
            
            
        