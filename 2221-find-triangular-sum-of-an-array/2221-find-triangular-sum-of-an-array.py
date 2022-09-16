class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        length = len(nums)
        while length > 1:
            
            for i in range(length-1):
                nums[i] = (nums[i]+nums[i+1]) % 10
            
            length -= 1
            
        
        return nums[0]