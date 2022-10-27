import random
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.stack)
        self.stack.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        index = self.dic[val]
        self.stack[index] = self.stack[-1]
        self.dic[self.stack[-1]] = index
        
        self.stack.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()