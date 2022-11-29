class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda x: x[1])
        
        current = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < current:
                count += 1
            else:
                current = intervals[i][1]
        
        return count
        