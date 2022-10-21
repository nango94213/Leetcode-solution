import collections
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        graph = collections.defaultdict(set)
        
        for i, v in enumerate(arr):
            graph[v].add(i)
            
        target = len(arr) - 1
        
        q = collections.deque([0])
        seen = set([0])
        
        jump = 0
        
        while q:
            for _ in range(len(q)):
                
                current = q.popleft()
                
                if current == target:
                    return jump
                
                left = current - 1
                right = current + 1
                same = graph[arr[current]]
                
                if left >= 0 and left not in seen:
                    seen.add(left)
                    q.append(left)
                
                if right <= target and right not in seen:
                    seen.add(right)
                    q.append(right)
                
                for s in same:
                    if s not in seen:
                        seen.add(s)
                        q.append(s)
                
                del graph[arr[current]]
            
            jump += 1
        
         