import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        dp = [[0, 0]]
        
        info = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    
        for s, e, p in info:
            index = bisect.bisect_right(dp, [s, float('inf')]) - 1
 
            if dp[index][1] + p > dp[-1][-1]:
                dp.append([e, dp[index][1] + p])
        return dp[-1][-1]