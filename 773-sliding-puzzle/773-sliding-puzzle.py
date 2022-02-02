import bisect
import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        directions = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        
        state = ''.join([str(c) for c in board[0]] + [str(c) for c in board[1]])
        
        start = state.index('0')
        
        seen = set([(start, state)])
        
        steps = 0

        q = collections.deque([(start, state)])
        
        while q:
            for _ in range(len(q)):
                
                current, state = q.popleft()
                
                if state == '123450':
                    return steps
                
                for d in directions[current]:
                    temp  = list(state)
                    temp[current], temp[d] = temp[d], temp[current]
                    temp = ''.join(temp)
                    
                    if (d, temp) not in seen:
                        seen.add((d, temp))
                        q.append((d, temp))
            
            steps += 1
        return -1
         
        return steps
                
                