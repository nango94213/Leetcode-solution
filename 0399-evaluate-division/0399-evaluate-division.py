class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = collections.defaultdict(defaultdict)
        
        for i, e in enumerate(equations):
            graph[e[0]][e[1]] = values[i]
            graph[e[1]][e[0]] = 1.0 / values[i]
        
        def check(start, end):
            
            q = collections.deque([(1.0, start)])
            seen = set([start])
            
            while q:
                current = q.popleft()
                
                if current[1] == end:
                    return current[0]
                
                for o in graph[current[1]]:
                    if o not in seen:
                        seen.add(o)
                        q.append((current[0]*graph[current[1]][o], o))
            
            
            return -1.0
        
        res = []
        
        for s, e in queries:
            if s not in graph or e not in graph:
                res.append(-1.0)
            
            elif s == e:
                res.append(1.0)
            else:
                res.append(check(s, e))
        
        return res