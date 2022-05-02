class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        res = 0
        
        for i in range(len(nums)):
            l = nums[i]
            r = nums[i]
            
            for j in range(i, len(nums)):
                
                l = min(l, nums[j])
                r = max(r, nums[j])
                
                res += (r-l)
        
        return res
        