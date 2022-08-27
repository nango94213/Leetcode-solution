class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        dp = 0
        total = 0
        
        for i in range(2, len(nums)):
            
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
            else:
                dp = 0
            total += dp
        
        return total