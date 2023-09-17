class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dic = {}
        
        for i in range(len(graph)):
            if i not in dic:
                dic[i] = True
                
                q = collections.deque([(i, True)])
                
                while q:
                    current, group = q.popleft()
                    
                    for n in graph[current]:
                        if n in dic and dic[n] == group:
                            return False
                        if n not in dic:
                            dic[n] = not group
                            q.append((n, not group))
        
        
        return True
        