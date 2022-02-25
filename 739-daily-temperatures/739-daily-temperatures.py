class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        
        stack = []
        
        
        for i, v in enumerate(temperatures):
            
            while stack and temperatures[stack[-1][0]] < v:
                index, t = stack.pop()
                res[index] = i - index
            
            stack.append((i,v))
            
        return res
        