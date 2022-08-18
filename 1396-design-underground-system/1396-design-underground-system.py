import collections
class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.totalTime = collections.defaultdict(lambda: [0, 0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startName, startTime = self.customer[id]
        
        self.totalTime[(startName, stationName)][0] += (t - startTime)
        self.totalTime[(startName, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.totalTime[(startStation, endStation)][0] / self.totalTime[(startStation, endStation)][1]       


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)