import random
class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.dic = {}
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.stack.append(val)
        self.dic[val] = len(self.stack) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        index = self.dic[val]
        last = self.stack[-1]
        self.stack[index] = last
        self.stack.pop()
        self.dic[last] = index
        del self.dic[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()