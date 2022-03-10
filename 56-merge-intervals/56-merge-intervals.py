class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        stack = [intervals[0]]
        
        for i in intervals:
            
            if stack[-1][1] < i[0]:
                stack.append(i)
            else:
                stack[-1][1] = max(stack[-1][1], i[1])
        return stack