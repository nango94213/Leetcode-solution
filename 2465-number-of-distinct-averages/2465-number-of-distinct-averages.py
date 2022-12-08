class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()
        
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        
        while left < right:
            res.add(nums[left]+nums[right])
            left += 1
            right -= 1
            
        return len(res)
        