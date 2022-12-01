class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        final1 = left
        left = 0
        right = len(nums) - 1
       
        while left <= right:
            mid = (left+right) // 2
    
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid -1
        final2 = left
  
        if nums[final1] != target:
            return [-1, -1]
        
        return [final1, final2-1]