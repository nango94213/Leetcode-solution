class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = 0
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid
        return nums[0]