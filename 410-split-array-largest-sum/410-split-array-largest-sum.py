class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        l = max(nums)
        r = sum(nums)
        
        while l < r:
            mid = (l+r) // 2
            
            num_sub = 1
            
            current_sum = 0
            
            for n in nums:
                
                if current_sum + n > mid:
                    num_sub += 1
                    current_sum = n
                
                else:
                    current_sum += n
            
            if num_sub > m:
                l = mid + 1
            else:
                r = mid
        
        return l
            
            