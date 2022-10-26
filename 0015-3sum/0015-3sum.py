class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        
        def twosum(index):
            
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                sum_three = nums[index] + nums[left] + nums[right]
                
                if sum_three == 0:
                    res.append([nums[index], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    
                elif sum_three < 0:
                    left += 1
                else:
                    right -= 1
        
        
        for i in range(len(nums)-2):
            
            if nums[i] > 0:
                break
            
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            twosum(i)
        
        return res