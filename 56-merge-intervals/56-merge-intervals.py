class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        stack = [intervals[0]]
        
        for i in intervals[1:]:
            
            if stack[-1][1] >= i[0]:
                stack[-1][1] = max(stack[-1][1], i[1])
                continue
            
            stack.append(i)
        
        return stack
        
        