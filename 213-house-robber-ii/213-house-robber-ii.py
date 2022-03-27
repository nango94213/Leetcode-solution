class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        two = nums[0]
        one = max(nums[0], nums[1])
        
        for i in range(2, len(nums)-1):
            two, one = one, max(two+nums[i], one)
        
        
        nums = nums[::-1]
        
        two1 = nums[0]
        one1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)-1):
            two1, one1 = one1, max(two1+nums[i], one1)
            
        return max(one, one1)