import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        self.dic[key] = value
        self.dic.move_to_end(key)
        
        if len(self.dic) > self.capacity:
            self.dic.popitem(False)
         


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)