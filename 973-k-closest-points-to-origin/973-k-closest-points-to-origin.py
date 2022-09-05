import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        
        for p in points:
            distance = ((p[0]-0)**2+(p[1]-0)**2)**0.5
            
            heapq.heappush(heap, (-distance, p))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]
        
                
        