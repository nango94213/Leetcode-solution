import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dic = collections.defaultdict(dict)
        res = float('inf')
        
        for f in flights:
            dic[f[0]][f[1]] = f[2]
        
        q = collections.deque([(src)])
        
        cost = collections.defaultdict(lambda: float('inf'))
        cost[(src, 0)] = 0
        
        stops = 0
        
        while q and stops <= k + 1:
            for _ in range(len(q)):
                
                current = q.popleft()
                if current == dst:
                  
                    res = min(res, cost[(current, stops)])
                    continue
                
                for o, v in dic[current].items():
                    
                    currentCost = cost[(current, stops)]
                   
                    if currentCost + v < cost[(o, stops+1)]:
                        cost[(o, stops+1)] = currentCost + v
                        q.append(o)
            
            stops += 1
        print(res)
        return res if res != float('inf') else -1

        