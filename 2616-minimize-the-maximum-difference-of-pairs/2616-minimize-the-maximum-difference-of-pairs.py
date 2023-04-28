class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        
        while left < right:
            mid = (left+right) // 2
            
            i = 1
            k = 0
            
            while i < len(nums):
                dif = nums[i] - nums[i-1]
                if dif <= mid:
                    k += 1
                    i += 2
                else:
                    i += 1
            
            if k >= p:
                right = mid
            else:
                left = mid + 1
        return left