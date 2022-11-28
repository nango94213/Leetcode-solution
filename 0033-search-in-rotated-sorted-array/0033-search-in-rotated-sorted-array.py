class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pivot = 0
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                pivot = mid + 1
                break
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid
        if pivot == 0 or target < nums[0]:
            left = pivot
            right = len(nums) - 1
        else:
            left = 0
            right = pivot - 1
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left += 1
            else:
                right -= 1
        
        return -1