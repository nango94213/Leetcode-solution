import random
class RandomizedSet:

    def __init__(self):
        
        self.value = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        
        if val in self.dic:
            return False
        
        self.value.append(val) 
        self.dic[val] = len(self.value) - 1
        
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.dic:
            return False
        
        last, index = self.value[-1], self.dic[val]
        
        self.value[index], self.dic[last] = last, index
        
        self.value.pop()
        
        del self.dic[val]
        
        return True
        


    def getRandom(self) -> int:
        
        return random.choice(self.value)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()