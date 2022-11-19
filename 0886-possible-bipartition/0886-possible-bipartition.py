import collections
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        group = {}
        graph = collections.defaultdict(set)
        
        for d in dislikes:
            graph[d[0]].add(d[1])
            graph[d[1]].add(d[0])
        
        
        for i in range(n):
            if i not in group:
                group[i] = True
                
                q = collections.deque([(i, True)])
                
                while q:
                    current, g = q.popleft()
                    
                    for o in graph[current]:
                        if o in group and group[o] == g:
                            return False
                        if o not in group:
                            group[o] = not g
                            q.append((o, not g))
        return True
    