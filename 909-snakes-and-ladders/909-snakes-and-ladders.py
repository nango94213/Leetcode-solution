import collections
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        dic = {1:0}
        q = collections.deque([1])
        n = len(board)
        while q:

            current = q.popleft()
            
            for i in range(current+1, current+7):
                
                x = (i-1) // n
                y = (i-1) % n
                
               
   
                nextN = board[-(x+1)][y if x % 2 == 0 else -(y+1)]

                if nextN > 0:
                    i = nextN

                if i == n * n:
                    return dic[current] + 1
                
                if i not in dic:
                    dic[i] = dic[current] + 1
                    q.append(i)
        
        return -1
            
        
        
        