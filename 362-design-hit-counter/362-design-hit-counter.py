import collections
class HitCounter:

    def __init__(self):
        self.dic = collections.defaultdict(lambda : 0)
        

    def hit(self, timestamp: int) -> None:
        self.dic[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        count = 0
        keys = list(self.dic.keys())
        
        for k in keys:
            if timestamp - k < 300:
                count += self.dic[k]
            else:
                del self.dic[k]
        
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)