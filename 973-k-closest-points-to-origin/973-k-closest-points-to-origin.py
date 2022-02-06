import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for i in points:
            distance=-(i[0]**2+i[1]**2)
            heapq.heappush(heap,(distance,i[0],i[1]))
            if len(heap)>k:
                heapq.heappop(heap)
        return [[x[1],x[2]] for x in heap ]