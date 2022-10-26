class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        offset = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                offset += 1
                continue
            
            nums[i-offset], nums[i] = nums[i], nums[i-offset]
        
        return nums