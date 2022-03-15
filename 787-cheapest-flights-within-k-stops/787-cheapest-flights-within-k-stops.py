import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        res = float('inf')
        
        dic = collections.defaultdict(collections.defaultdict)
        
        for f in flights:
            dic[f[0]][f[1]] = f[2]
        
        
        stops = 0
        
        q = collections.deque([src])
        
        cost = collections.defaultdict(lambda: float('inf'))
        
        cost[(src, 0)] = 0
        
        while q and stops <= k+1:
            
            for _ in range(len(q)):
                
                current = q.popleft()
                
                if current == dst:

                    res = min(res, cost[(current, stops)])
                    continue
                
                for outgoing, value in dic[current].items():
      
                    current_cost = cost[(current, stops)]
                    next_cost = value
                    
                    if current_cost + next_cost < cost[(outgoing, stops+1)]:
                        q.append(outgoing)
                        
                        cost[(outgoing, stops+1)] = current_cost + next_cost
            
            stops += 1
        
        return res if res != float('inf') else -1
                    
        