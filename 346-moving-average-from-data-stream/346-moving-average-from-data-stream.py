import collections
class MovingAverage:

    def __init__(self, size: int):
        
        self.size = size
        self.stack = collections.deque()
        

    def next(self, val: int) -> float:
        
        self.stack.append(val)
        
        if len(self.stack) > self.size:
            self.stack.popleft()
            
        
        return sum(self.stack)  / len(self.stack)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)