class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        [1, 3, 12, 0, 0]
        
        index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
                
        