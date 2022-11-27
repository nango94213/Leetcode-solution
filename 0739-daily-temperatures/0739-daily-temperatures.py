class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = []
        
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                tmp = stack.pop()
                res[tmp] = i - tmp
            
            stack.append(i)
        
        return res
        
        