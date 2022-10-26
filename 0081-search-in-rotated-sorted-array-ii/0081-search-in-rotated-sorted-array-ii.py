class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        pivot = 0
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # shifting to remove duplicate elements
            while left<right and nums[left] == nums[left+1]:
                left+=1
            while left<right and nums[right] == nums[right-1]:
                right-=1
            if left == right:
                break
            mid = (left+right) // 2
            if nums[mid] > nums[mid+1]:
                pivot = mid + 1
                break
             
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid

        if pivot == 0 or target < nums[0]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] < target:
                l = mid + 1
            
            if nums[mid] > target:
                r = mid - 1
        
        return False
        