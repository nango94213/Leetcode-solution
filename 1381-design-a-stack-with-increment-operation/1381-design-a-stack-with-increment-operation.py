class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if not self.inc:
            return
        self.inc[min(k, len(self.inc)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)