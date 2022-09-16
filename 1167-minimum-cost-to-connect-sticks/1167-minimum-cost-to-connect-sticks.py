import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            
            res += cost
            
            heapq.heappush(sticks, cost)
        
        return res
            
        