import random
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.number = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        
        self.dic[val] = len(self.number)
        self.number.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        index, lastn = self.dic[val], self.number[-1]
        
        self.number[index], self.dic[lastn] = lastn, index
        
        self.number.pop()
        del self.dic[val]
        
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.number)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()