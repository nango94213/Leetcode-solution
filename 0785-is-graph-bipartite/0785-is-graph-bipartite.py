import collections
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        dic = {}
        
        for i in range(len(graph)):
            if i not in dic:
                dic[i] = True
                
                q = collections.deque([(i, True)])
                
                while q:
                    current, group = q.popleft()
                    
                    for d in graph[current]:
                        if d in dic and dic[d] == group:
                            return False
                        
                        if d not in dic:
                            dic[d] = not group
                            q.append((d, not group))
        
        return True