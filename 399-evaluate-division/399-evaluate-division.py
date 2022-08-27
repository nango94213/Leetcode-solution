import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        res = []
        graph = collections.defaultdict(defaultdict)
        
        for e, v in zip(equations, values):
            graph[e[0]][e[1]] = v
            graph[e[1]][e[0]] = 1 / v
            
        
        def bfs(start, target):
            
            q = collections.deque([(start, 1.0)])
            
            seen = set([start])
            
            while q:
                
                current, value = q.popleft()
                
                if current == target:
                    return value
                
                for neighbor in graph[current]:
                    if neighbor not in seen:
                        
                        seen.add(neighbor)
                        q.append((neighbor, value * graph[current][neighbor]))
            
            return  -1.0
        
        for s, t in queries:
            if s not in graph or t not in graph:
                res.append(-1.0)
                continue
            
            if s == t:
                res.append(1.0)
                continue
            
            res.append(bfs(s, t))
        
        return res
        
            
        
        