import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        meet = []
        
        intervals.sort()
        
        for i in intervals:
            
            if meet and meet[0] <= i[0]:
                
                heapq.heappop(meet)
                
            
            heapq.heappush(meet, i[1])
        
        return len(meet)
        
        
        
        