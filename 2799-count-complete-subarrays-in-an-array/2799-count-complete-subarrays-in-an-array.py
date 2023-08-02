class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        
        count = Counter()
        
        left = 0
        res = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) == target:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += left 
        
        return res
            
            
        