class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse = True)
        
        res = 1
        start = nums[0]
        
        for n in nums:
            
            if start - n > k:
                res += 1
                start = n
        
        return res
        