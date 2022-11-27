import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()
        res = []
        
        for i in intervals:
            if res and i[0]>= res[0]:
                heapq.heappop(res)
            
            heapq.heappush(res, i[1])
        
        return len(res)
        
        