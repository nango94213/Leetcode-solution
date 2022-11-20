class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left+right) // 2
            
            current = 0
            total = 1
            
            for n in nums:
                if current + n > mid:
                    current = n
                    total += 1
                else:
                    current += n
            
            if total > k:
                left = mid + 1
            else:
                right = mid
        
        return left