import collections
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        currentMax = collections.deque()
        currentMin = collections.deque()
        
        left = 0
        res = 0
        
        for right, value in enumerate(nums):
            
            while currentMax and nums[currentMax[-1]] <= value:
                currentMax.pop()
            
            while currentMin and nums[currentMin[-1]] >= value:
                currentMin.pop()
            
            currentMax.append(right)
            currentMin.append(right)
            
            while nums[currentMax[0]] - nums[currentMin[0]] > limit:
                left += 1
                
                if left > currentMax[0]:
                    currentMax.popleft()
                
                if left > currentMin[0]:
                    currentMin.popleft()
            
            res = max(res, right-left+1)
        
        return res