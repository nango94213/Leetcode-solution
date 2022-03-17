import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        graph = collections.defaultdict(set)
        
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
            
        
        count = 0
        
        
        
        checked = set()
        
        for i in range(n):
            if i not in checked:
                checked.add(i)
                count += 1
                
                q = collections.deque([i])
                
                while q:
                    
                    current = q.popleft()
                    
                    for neighbor in graph[current]:
                        
                        if neighbor not in checked:
                            checked.add(neighbor)
                            q.append(neighbor)
        
        return count
        