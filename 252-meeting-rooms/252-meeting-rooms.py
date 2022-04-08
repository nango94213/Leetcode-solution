class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        
        if not intervals:
            return True
        
        intervals.sort()
        
        current = intervals[0][1]
        
        for i in intervals[1:]:
            
            if i[0] < current:
                return False
            
            current = i[1]
        
        return True
        