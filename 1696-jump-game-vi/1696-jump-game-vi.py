import collections
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        q = collections.deque([0])
        
        for i in range(1, len(nums)):
            
            if q and q[0] < i - k:
                q.popleft()
            
            dp[i] = dp[q[0]] + nums[i]
            
            while q and dp[q[-1]] < dp[i]:
                q.pop()
            
            q.append(i)
        
        return dp[-1]
        
        