import collections
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        group = collections.defaultdict(set)
        
        for i, v in enumerate(arr):
            group[v].add(i)
        
        q = collections.deque([0])
        
        seen = set([0])
        
        jump = 0
        
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                
                if current == len(arr) - 1:
                    return jump
                
                if current + 1 < len(arr) and current + 1 not in seen:
                    q.append(current+1)
                    seen.add(current+1)
                
                if current - 1 >= 0 and current - 1 not in seen:
                    q.append(current-1)
                    seen.add(current-1)
                    
                for o in group[arr[current]]:
                    if o not in seen:
                        q.append(o)
                        seen.add(o)
                
                del group[arr[current]]
            
            jump += 1
        
        return jump
        
        