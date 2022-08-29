class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        
                        nums[i], nums[j] = nums[j], nums[i]
                        
                        
                        left = i + 1
                        right = len(nums) - 1
                        
                        while left < right:
                            
                            nums[left], nums[right] = nums[right], nums[left]
                            
                            left += 1
                            right -= 1
                        
                        return
        
        nums.reverse()