class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        pivot = 0
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l+r) // 2
            
            if nums[mid] > nums[mid+1]:
                pivot = mid + 1
            
            if nums[mid] > nums[0]:
                l = mid + 1
            
            else:
                r = mid
        
        return min(nums[0], nums[pivot])
        