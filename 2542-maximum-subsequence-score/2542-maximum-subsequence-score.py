import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        tmp = sorted(list(zip(nums1, nums2)), key=lambda x:x[1], reverse=True)
        
        h = []
        
        res = 0
        total = 0
        for i, (a, b) in enumerate(tmp):
            
            heapq.heappush(h, a)
            total += a
            if len(h) > k:
                total -= heapq.heappop(h)
            
            if i >= k - 1:
                res = max(res, total * b)
        
        return res
            
        
        