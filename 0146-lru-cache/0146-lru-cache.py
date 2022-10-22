class DoubleLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
class LRUCache:
    
    def addNode(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        
        self.tail.prev.next = node
        self.tail.prev = node
    
    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    
    def moveToEnd(self, node):
        self.removeNode(node)
        self.addNode(node)
    
    def popOld(self):
        
        res = self.head.next
        self.removeNode(res)
        
        return res

    def __init__(self, capacity: int):
        self.dic = {}
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        
        if key in self.dic:
            node = self.dic[key]
            self.moveToEnd(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            node = self.dic[key]
            self.moveToEnd(node)
            node.value = value
        else:
            node = DoubleLinkedNode()
            node.key = key
            node.value = value
            self.size += 1
            
            self.addNode(node)
            self.dic[key] = node
            
            if self.size > self.capacity:
                oldNode = self.popOld()
                self.size -= 1
                del self.dic[oldNode.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)