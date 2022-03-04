import collections
class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.time = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_time = self.customer[id]
        self.time[(start, stationName)][0] += t-start_time
        self.time[(start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.time[(startStation, endStation)]
        return total/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)