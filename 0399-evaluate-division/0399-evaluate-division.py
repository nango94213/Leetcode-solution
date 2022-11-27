import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(defaultdict)
        
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
        
        def check(s, e):
            q = collections.deque([(s, 1.0)])
            seen = set([s])
            while q:
                current, value = q.popleft()
                if current == e:
                    return value
                for o in graph[current].keys():
                    if o not in seen:
                        seen.add(o)
                        q.append((o, graph[current][o]*value))
            
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
        