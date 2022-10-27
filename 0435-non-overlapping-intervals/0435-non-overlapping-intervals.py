class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        
        prev = intervals[0]
        count = 0
        
        for i in intervals[1:]:
            if i[0] >= prev[1]:
                prev = i
            else:
                count += 1
        
        return count
        