import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        meeting = []
        
        for i in intervals:
            if meeting and meeting[0] <= i[0]:
                heapq.heappop(meeting)
            
            heapq.heappush(meeting, i[1])
        
        return len(meeting)
        