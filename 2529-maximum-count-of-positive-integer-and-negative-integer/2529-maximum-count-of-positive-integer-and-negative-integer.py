class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        pivot = 0
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] < 0 and nums[mid+1] >= 0:
                pivot = mid
                break
            
            if nums[mid] < 0:
                left = mid + 1
            if nums[mid] >= 0:
                right = mid - 1
        left = 0
        right = len(nums) - 1
        pivot1 = 0
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] > 0 and nums[mid-1] <= 0:
                pivot1 = mid
                break
            
            if nums[mid] > 0:
                right = mid - 1
            if nums[mid] <= 0:
                left = mid + 1
        
        if pivot1 == 0:
            return len(nums) if nums[0] > 0 else 0
        else:
            return max(pivot+1, len(nums)-pivot1)