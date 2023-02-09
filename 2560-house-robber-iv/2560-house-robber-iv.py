class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)
        
        while left < right:
            mid = (left+right) // 2
            switch = False
            total = 0
            for n in nums:
                if not switch:
                    if n > mid:
                        continue
                    total += 1
                    switch = True
                else:
                    switch = False
                    continue
            if total < k:
                left = mid + 1
            else:
                right = mid
        return left