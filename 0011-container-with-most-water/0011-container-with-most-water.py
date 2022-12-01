class Solution:
    def maxArea(self, height: List[int]) -> int:
        nums = height
        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            res = max(res, min(nums[left], nums[right]) * (right-left))
            
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        
        return res
            
        