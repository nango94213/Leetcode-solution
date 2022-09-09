import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        graph = collections.defaultdict(collections.defaultdict)
        
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
                        q.append((neighbor, value*graph[current][neighbor]))
            
            return -1.0
        
        
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                res.append(-1.0)
                continue
            
            if q[0] == q[1]:
                res.append(1.0)
                continue
            
            res.append(bfs(q[0], q[1]))
        
        return res
        