import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for i, v in enumerate(points):
            distance=-(v[0]**2+v[1]**2)
            heapq.heappush(heap,(distance,i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [points[x[1]] for x in heap]