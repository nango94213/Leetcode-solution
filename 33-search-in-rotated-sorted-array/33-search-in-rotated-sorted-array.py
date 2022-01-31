class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums) - 1
        pivot = 0
        
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                pivot = mid + 1
                break
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
  
        if target >= nums[0] and pivot != 0:
            l = 0
            r = pivot - 1
        else:
            l = pivot
            r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        