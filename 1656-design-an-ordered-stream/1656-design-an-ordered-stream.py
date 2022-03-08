class OrderedStream:

    def __init__(self, n: int):
        self.result = [0] * n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        index = idKey - 1
        
        self.result[index] = value
        
        if index > self.ptr:
            return []
        
        while self.ptr < len(self.result) and self.result[self.ptr]:
            self.ptr += 1
        
        return self.result[index:self.ptr]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)