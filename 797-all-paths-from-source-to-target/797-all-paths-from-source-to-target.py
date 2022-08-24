import collections
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        q = collections.deque([(0, [0])])
        target = len(graph) - 1
        res = []
        
        while q:
            
            current, path = q.popleft()
            
            if current == target:
                res.append(path)
                
            for nxt in graph[current]:
                q.append((nxt, path+[nxt]))
        
        return res
        