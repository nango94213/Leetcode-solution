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
                    
                        l = i + 1
                        r = len(nums) - 1
                    
                        while l < r:
                            nums[l], nums[r] = nums[r], nums[l]
                        
                            l += 1
                            r -= 1
                        return
        
        nums.reverse()
                        
            