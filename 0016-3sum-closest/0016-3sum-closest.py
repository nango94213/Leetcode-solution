class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = float('inf')
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                if abs(total - target) < abs(res - target):
                    res = total
                
                if total > target:
                    right -= 1
                
                if total < target:
                    left += 1
            
        
        return res
        