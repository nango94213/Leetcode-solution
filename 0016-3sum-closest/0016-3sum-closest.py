class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        diff = float('inf')
       
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                 
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    return target
                
                if abs(total - target) < abs(diff):
                    diff = total - target
                
                if total > target:
                    right -= 1
                
                if total < target:
                    left += 1
        
        return target + diff
                
        