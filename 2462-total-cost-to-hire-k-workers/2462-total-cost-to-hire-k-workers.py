import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        if candidates < len(costs) / 2:
            left = costs[:candidates]
            right = costs[-candidates:]
            remain = collections.deque(costs[candidates:-candidates])
        else:
            left = costs[:candidates]
            right = costs[candidates:]
            remain = []
        heapq.heapify(left)
        heapq.heapify(right)
        
        
        print(left)
        print(right)
        for _ in range(k):
            if not right:
                res += left[0]
                heapq.heappop(left)
                if remain:
                    heapq.heappush(left, remain.popleft())
                continue
            if not left:
                res += right[0]
                heapq.heappop(right)
                if remain:
                    heapq.heappush(right, remain.popl())
                continue    
            
            if left[0] > right[0]:
                res += right[0]
                heapq.heappop(right)
                if remain:
                    heapq.heappush(right, remain.pop())
            else:
                res += left[0]
                heapq.heappop(left)
                if remain:
                    heapq.heappush(left, remain.popleft())
            
        return res
        
        