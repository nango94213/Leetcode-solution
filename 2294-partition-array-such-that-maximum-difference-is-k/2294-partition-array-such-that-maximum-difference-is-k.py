class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        res = 1
        start = nums[0]
        
        for n in nums:
            
            if n - start > k:
                res += 1
                start = n
        
        return res