class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(n):
            res = 0
            
            count = Counter()
            left = 0
            for right in range(len(nums)):
                if count[nums[right]] == 0:
                    n -= 1
                count[nums[right]] += 1
                
                while n < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        n += 1
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return helper(k) - helper(k-1)