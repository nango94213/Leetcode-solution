class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        nums = [0] + nums + [0]
        stack = [-1]
        max_area = 0
        prefix = []
        current = 0
        
        for i in range(len(nums)):
            current += nums[i]
            prefix.append(current)
 
        for i in range(len(nums)):
     
            while nums[i] < nums[stack[-1]]:
                h = nums[stack.pop()]
                w = prefix[i-1] - prefix[stack[-1]]

                max_area = max(max_area, w*h)
                
            
            stack.append(i)
        
        return max_area % (10**9+7)