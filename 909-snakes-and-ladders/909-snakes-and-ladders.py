import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        seen = set([1])
        move = 0
        q = collections.deque([1])
        n = len(board)
        while q:

            for _ in range(len(q)):
                current = q.popleft()
                if current == n * n:
                    return move
                for i in range(current+1, current+7):
                
                       x = (i-1) // n
                       y = (i-1) % n
                
                       if 0 <= x < len(board) and 0 <= y < len(board[0]):
   
                                     nextN = board[-(x+1)][y if x % 2 == 0 else -(y+1)]

                                     if nextN > 0:
                                           i = nextN
                
                                     if i not in seen:
                                              seen.add(i)
                                              q.append(i)
            move += 1
        
        return -1
            
        
        
        