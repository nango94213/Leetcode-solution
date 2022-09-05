class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        
        arr = [float('-inf')] + arr + [float('-inf')]
        
        res = 0

        for i, v in enumerate(arr):
            
            while stack and arr[stack[-1]] > v:
                current = stack.pop()
                res += arr[current] * (current-stack[-1]) * (i-current)
            
            stack.append(i)
        
        return res % (10**9+7)
                