import heapq
class MedianFinder:

    def __init__(self):
        self.a = []
        self.b = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.a, -num)
        heapq.heappush(self.b, -self.a[0])
        heapq.heappop(self.a)
        
        if len(self.a) < len(self.b):
            heapq.heappush(self.a, -self.b[0])
            heapq.heappop(self.b)

    def findMedian(self) -> float:

        return -self.a[0] if len(self.a) > len(self.b) else (-self.a[0]+self.b[0]) / 2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()