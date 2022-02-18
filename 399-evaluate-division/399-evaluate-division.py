import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = collections.defaultdict(defaultdict)
        
        for e, v in zip(equations, values):
            graph[e[0]][e[1]] = v
            graph[e[1]][e[0]] = 1/v
        
        
        def bfs(start, end):
            
            q = collections.deque([(start, 1.0)])
            seen = set([start])
            while q:
                
                current, product = q.popleft()
                
                if current == end:
                    return product
                
                for neighbor, value in graph[current].items():
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append((neighbor, product*value))
            return -1.0
        
        res = []
        for q in queries:
            s, e = q
            if (s not in graph) or (e not in graph):
                res.append(-1.0)
            elif s == e:
                res.append(1.0)
            
            
            
            else:
                res.append(bfs(s, e))
        
        return res
            
        