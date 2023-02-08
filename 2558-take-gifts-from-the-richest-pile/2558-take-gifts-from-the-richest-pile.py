import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = list(map(lambda x:-x, gifts))
        heapq.heapify(heap)
        
        for _ in range(k):
            current = heapq.heappop(heap)
            heapq.heappush(heap, -math.floor((-current)**0.5))
        
        return -sum(heap)