class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        dic = {}
        
        for i in range(len(graph)):
            if i not in dic:
                dic[i] = True
                q = collections.deque([(i, True)])
                
                while q:
                    current, group = q.popleft()
                    
                    for o in graph[current]:
                        if o in dic and dic[o] == group:
                            return False
                        if o not in dic:
                            dic[o] = not group
                            q.append((o, not group))
        return True
                
        