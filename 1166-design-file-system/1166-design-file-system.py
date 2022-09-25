import collections
class FileSystem:

    def __init__(self):
        self.dic = dict()
        self.dic[""] = 100

    def createPath(self, path: str, value: int) -> bool:
        if (path in self.dic) or ((path[:path.rfind("/")] not in self.dic)):
            return False
        
        self.dic[path] = value
        
        return True
        

    def get(self, path: str) -> int:
        
        if  path in self.dic:
            return self.dic[path]
        else:
            return -1

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)