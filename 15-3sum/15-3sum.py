class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        res = []
        
        def twosum(i):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i == 0 or nums[i] != nums[i-1]:
                twosum(i)
        
        return res
                        
                
                