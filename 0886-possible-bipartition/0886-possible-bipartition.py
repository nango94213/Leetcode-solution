import collections
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(set)
        
        for d in dislikes:
            graph[d[0]].add(d[1])
            graph[d[1]].add(d[0])
        
        seen = set()
        group = {}
        
        for i in range(1, n+1):
            if i not in group:
                group[i] = True
     
                
                q = collections.deque([(i, True)])
                
                while q:
                    
                    current, label = q.popleft()
                    
                    for child in graph[current]:
                        if (child in group) and (group[child] == label):
                            return False
                        
                        
                        
                        if child not in group:
                            group[child] = not label
                            q.append((child, not label))
        
        return True
                        