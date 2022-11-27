import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        
        seen = set()
        
        count = 0
        
        for i in range(n):
            if i not in seen:
                count += 1
                seen.add(i)
                q = collections.deque([i])
                
                while q:
                    current = q.popleft()
                    
                    for o in graph[current]:
                        if o not in seen:
                            seen.add(o)
                            q.append(o)
        return count