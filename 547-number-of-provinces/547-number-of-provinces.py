import collections
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        graph = collections.defaultdict(set)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        
        
        seen = set()
        res = 0

        for k in range(len(isConnected)):
            if k not in seen:
                seen.add(k)
                res += 1
                
                q = collections.deque([k])
                
                while q:
                    
                    current = q.popleft()
                    
                    for nextOne in graph[current]:
                        if nextOne not in seen:
                            seen.add(nextOne)
                            q.append(nextOne)
        
        return res
                
        