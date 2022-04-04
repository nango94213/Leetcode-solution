class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals, key=lambda x:x[1])
        
        current = intervals[0]
        count = 0
        
        for i in intervals[1:]:
            
            if i[0] < current[1]:
                count += 1
            else:
                current = i
        
        return count
                