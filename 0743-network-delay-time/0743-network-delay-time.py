import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dic = {}
        
        graph = collections.defaultdict(dict)
        
        for t in times:
            graph[t[0]][t[1]] = t[2]
        
        heap = [(0, k)]
        
        while heap:
            
            distance, current = heapq.heappop(heap)
            
            if current not in dic:
                dic[current] = distance
                
                for outgoing in graph[current]:
                    
                    heapq.heappush(heap, (distance+graph[current][outgoing], outgoing))
      
        if len(dic) == n:
            return max(dic.values())
        else:
            return -1
        