import heapq, math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        res = 0
        for i in range(k):
            
            current = - heapq.heappop(nums)
    
            res += current
            
            heapq.heappush(nums, -math.ceil(current/3))
        
        return res
            
            