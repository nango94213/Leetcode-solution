class bucket():
    def __init__(self):
        self.buc=[]
    def put(self,key,value):
        found=False
        for i in range(len(self.buc)):
            if key==self.buc[i][0]:
                self.buc[i]=(key,value)
                found=True
                break
        if not found:
            self.buc.append((key,value))
            
    def get(self,key):
        for k,v in self.buc:
            if k==key:
                return v
        return -1
                
    def remove(self,key):
        for i,kv in enumerate(self.buc):
            if kv[0]==key:
                del self.buc[i]
            
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space=2069
        self.hashmap=[bucket() for i in range(self.key_space)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hashkey=key%self.key_space
        self.hashmap[hashkey].put(key,value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashkey=key%self.key_space
        return self.hashmap[hashkey].get(key)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashkey=key%self.key_space
        self.hashmap[hashkey].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)