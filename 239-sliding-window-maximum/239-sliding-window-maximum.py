import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = collections.deque()
        
        res = []
        
        for i, v in enumerate(nums):
            
            while q and v > nums[q[-1]]:
                q.pop()
            
            q.append(i)
            
            if i - q[0] +1 > k:
                q.popleft()
            
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res
            
        
        