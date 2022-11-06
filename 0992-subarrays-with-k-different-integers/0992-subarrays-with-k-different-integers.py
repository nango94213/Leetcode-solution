class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(nums, x):
            
            left = 0
            count = Counter()
            res = 0
            
            for right in range(len(nums)):
                
                if count[nums[right]] == 0:
                    x -= 1
                
                count[nums[right]] += 1
                
                while x < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        x += 1
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return helper(nums, k) - helper(nums, k-1)
        