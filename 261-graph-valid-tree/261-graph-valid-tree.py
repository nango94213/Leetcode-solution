import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        dic = collections.defaultdict(set)
        
        for e in edges:
            dic[e[0]].add(e[1])
            
            dic[e[1]].add(e[0])
        
        seen = set([0])
    
                
        q  = collections.deque([(-1, 0)])
        res = []

        while q:
                    
                    parent, current = q.popleft()
                    res.append(current) 
                    for o in dic[current]:
                        if o != parent and o in seen:
           
                            return False
                        if o not in seen:
                           seen.add(o)
                           q.append((current, o))

                
        return len(res) == n
            
        