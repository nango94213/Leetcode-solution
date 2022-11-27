class gg:
    def __init__(self):
        self.v = 0
        self.k = 0
        self.next = None
        self.prev = None
class LRUCache:
    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        
        self.tail.prev.next = node
        self.tail.prev = node
  
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def update(self, node):
        self.remove(node)
        self.add(node)
    
    def pop(self):
        h = self.head.next
        self.remove(h)
        return h

    def __init__(self, capacity: int):
        self.dic = {}
        self.head = gg()
        self.tail = gg()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.c = capacity
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.update(self.dic[key])
        return self.dic[key].v
        

    def put(self, key: int, value: int) -> None:
   
        if key in self.dic:
            self.dic[key].v = value
            self.update(self.dic[key])
        else:
            node = gg()
            node.k = key
            node.v = value
            self.add(node)
            self.dic[key] = node
            if len(self.dic) > self.c:
                tmp = self.pop()

                del self.dic[tmp.k]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)