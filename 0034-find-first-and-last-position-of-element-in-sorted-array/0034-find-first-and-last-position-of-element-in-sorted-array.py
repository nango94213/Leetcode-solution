import bisect
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
            a = left
            if nums[a] != target:
                a = -1
            
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left+right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            b = right 
            if nums[b] != target:
                if nums[b-1] == target:
                    b -= 1
                else:
                    b = -1
            
            return [a, b]
        