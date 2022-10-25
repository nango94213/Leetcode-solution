import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(set)
        
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        
        q = collections.deque([(0, -1)])
        
        seen = set([0])
        
        res = 0
        
        while q:
            current, parent = q.popleft()
            res += 1
            
            for outgoing in graph[current]:
                if outgoing != parent and outgoing in seen:
                    return False
                if outgoing not in seen:
                    q.append((outgoing, current))
                    seen.add(outgoing)
        
        return res == n