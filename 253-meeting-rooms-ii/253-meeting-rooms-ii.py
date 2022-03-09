import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        h = []
    
        

        
        for i in intervals:
            
            if h and i[0] >= h[0]:
                heapq.heappop(h)
            
            
            heapq.heappush(h, i[1])
        

        
        return len(h)
            
        