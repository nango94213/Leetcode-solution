import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = {0:(1, 3), 1:(0, 2, 4), 2:(1, 5), 3:(0, 4), 4:(1, 3, 5), 5:(2, 4)}
        
        state = ''.join([str(i) for i in board[0]]) + ''.join([str(i) for i in board[1]])
        
        q = collections.deque([state])
        seen = set([state])
        step = 0
        
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current == '123450':
                    return step
                
                index = current.index('0')
                
                for o in directions[index]:
                    l = list(current)
                    l[o], l[index] = l[index], l[o]
                    s = ''.join(l)
                    if s not in seen:
                        seen.add(s)
                        q.append(s)
            step += 1
        
        return -1
                    