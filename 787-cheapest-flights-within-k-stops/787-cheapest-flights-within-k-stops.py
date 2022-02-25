import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        
        
        dic = collections.defaultdict(list)
        
        for f in flights:
            dic[f[0]].append((f[1], f[2]))
        
        
   
        
        q = collections.deque([src])
        
        steps = 0
        min_price = float('inf')
        dp = collections.defaultdict(lambda: float('inf'))
        dp[(src, 0)] = 0
        while q and steps<=k+1:
            for _ in range(len(q)):
                
                
                current = q.popleft()
                
          
                if current == dst:
                    min_price = min(min_price, dp[(current, steps)])
          
          
                 
                for outgoing in dic[current]:
                    cost_now = dp[(current, steps)] 
                    cost_outgoing = dp[(outgoing[0], steps+1)] 
                    
                    if outgoing[1] + cost_now < cost_outgoing:
                        q.append(outgoing[0])
                        dp[(outgoing[0], steps+1)] = outgoing[1] + cost_now
          
            steps += 1
        
        return min_price if min_price != float('inf') else -1
                
            
                
            
            