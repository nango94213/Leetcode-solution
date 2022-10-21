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
            if i not in seen:
                group[i] = True
                seen.add(i)
                
                q = collections.deque([(i, True)])
                
                while q:
                    
                    current, label = q.popleft()
                    
                    for child in graph[current]:
                        if (child in group) and (group[child] == label):
                            return False
                        
                        group[child] = not label
                        
                        if child not in seen:
                            seen.add(child)
                            q.append((child, not label))
        
        return True
                        