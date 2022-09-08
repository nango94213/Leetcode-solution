import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-k, v) for v, k in Counter(s).items()]
        heapq.heapify(heap)
        
        pre_num, pre_c = 0, ''
        res = []
        
        while heap:
            num, c = heapq.heappop(heap)
            
            res.append(c)
            
            num += 1
            
            if pre_num < 0:
                heapq.heappush(heap, (pre_num, pre_c))
            
            pre_num, pre_c = num, c
 
        
        return ''.join(res) if len(res) == len(s) else ''
        