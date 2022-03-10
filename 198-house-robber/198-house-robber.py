class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        a=[0]*len(nums)
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        a[0]=nums[0]
        a[1]=max(nums[1],nums[0])
        
        
        for i in range(2,len(nums)):
            a[i]=max(nums[i]+a[i-2],a[i-1])
        return max(a)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            
            
        
        
       