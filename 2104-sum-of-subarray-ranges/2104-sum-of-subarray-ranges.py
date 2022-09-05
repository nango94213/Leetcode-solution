class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        '''res = 0
        
        for i in range(len(nums)):
            l = nums[i]
            r = nums[i]
            
            for j in range(i, len(nums)):
                
                l = min(l, nums[j])
                r = max(r, nums[j])
                
                res += (r-l)
        
        return res'''
        
        stack = []
        stack2 = []
        
        arr = [float('-inf')] + nums + [float('-inf')]
        arr2 = [float('inf')] + nums + [float('inf')]
        
        res = 0
        
        for i, v in enumerate(arr2):
            
            while stack2 and arr2[stack2[-1]] < v:
                current = stack2.pop()
                res += arr2[current] * (current-stack2[-1]) * (i-current)
            stack2.append(i)
            
        for i, v in enumerate(arr):
            
            while stack and arr[stack[-1]] > v:
                current = stack.pop()
                res -= arr[current] * (current-stack[-1]) * (i-current)
            
            stack.append(i)
      
        
 
        return res
        