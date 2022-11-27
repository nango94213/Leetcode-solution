import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        
        for f in flights:
            graph[f[0]][f[1]] = f[2]
        
        q = collections.deque([(src, 0)])
        seen = collections.defaultdict(lambda: float('inf'))
        seen[(src, 0)] = 0
        
        stop = 0
        res = float('inf')
        while q and stop <= k + 1:
            for _ in range(len(q)):
                current, _ = q.popleft()
                if current == dst:
                    print(current)
                    res = min(res, seen[(current, stop)])
                    continue
            
                for o in graph[current]:
                    p = seen[(current, stop)]
                
                    if p + graph[current][o] < seen[(o, stop+1)]:
                        seen[(o, stop+1)] = p + graph[current][o]
                        q.append((o, stop+1))
            stop += 1
        return -1 if res == float('inf') else res
             