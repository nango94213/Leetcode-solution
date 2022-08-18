class OrderedStream:

    def __init__(self, n: int):
        self.result = [0] * n
        self.plt = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        index = idKey - 1
        self.result[index] = value
        
        if index > self.plt:
            return []
        
        while self.plt < len(self.result) and self.result[self.plt]:
            self.plt += 1
        
        return self.result[index:self.plt]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)