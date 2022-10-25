import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        dic = collections.defaultdict(set)
        
        for e in edges:
            dic[e[0]].add(e[1])
            dic[e[1]].add(e[0])
        
        seen = set()
        
        res = 0
        
        for i in range(n):
            if i not in seen:
                res += 1
                seen.add(i)
                q = collections.deque([i])
                
                while q:
                    current = q.popleft()
                    
                    for o in dic[current]:
                        if o not in seen:
                            seen.add(o)
                            q.append(o)
        
        return res