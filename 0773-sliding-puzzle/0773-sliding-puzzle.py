import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        
        state = ''.join([str(i) for i in board[0]]) + ''.join([str(i) for i in board[1]])
        
        start  = state.index('0')
        
        q = collections.deque([(start, state)])
        
        step = 0
        
        seen = set([state])
        
        while q:
            
            for _ in range(len(q)):
                current0, currentState = q.popleft()
                
                if currentState == '123450':
                    return step
                
                for d in directions[current0]:
                    tmp = list(currentState)
                    
                    tmp[current0], tmp[d] = tmp[d], tmp[current0]
                    
                    tmp = ''.join(tmp)
                    
                    if tmp not in seen:
                        seen.add(tmp)
                        q.append((d, tmp))
            
            step += 1
            
        return -1
                    