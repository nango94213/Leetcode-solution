class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        stack = []
        
        for i in intervals:
            
            if stack and stack[-1][1] >= i[0]:
                
                stack[-1][1] = max(stack[-1][1], i[1])
                
                continue
            
            stack.append(i)
        
        return stack