import collections
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = collections.deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        
        if num == self.value:
            if self.q and self.q[-1] == num:
                self.count += 1
            else:
                self.count = 1
        else:
            self.count = 0
        
        self.q.append(num)
        
        if len(self.q) > self.k:
            self.q.popleft()
        
        return self.count >= self.k
            
        
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)