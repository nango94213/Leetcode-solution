import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        h = []
        h.append(intervals[0][1])
        

        
        for i in intervals[1:]:
            
            if i[0] >= h[0]:
                heapq.heappop(h)
            
            heapq.heappush(h, i[1])
        

        
        return len(h)
            
        