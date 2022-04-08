class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        stack = []
        
        index = 0
        
        while index < len(intervals) and intervals[index][0] < newInterval[0]:
            
            stack.append(intervals[index])
            
            index += 1
        
        if stack and stack[-1][1] >= newInterval[0]:
            stack[-1][1] = max(stack[-1][1], newInterval[1])
        else:
            stack.append(newInterval)
        
        
        while index < len(intervals):
            
            if stack[-1][1] >= intervals[index][0]:
                stack[-1][1] = max(stack[-1][1], intervals[index][1])
            
            else:
                stack.append(intervals[index])
 
            index += 1
        
        return stack
        
        
        