class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack = []
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                current = stack.pop()
                res[current] = i - current
            
            stack.append(i)
        
        return res