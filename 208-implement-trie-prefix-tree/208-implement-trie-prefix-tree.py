class Trie:

    def __init__(self):
        self.t = {}

    def insert(self, word: str) -> None:
        
        tmp = self.t
        
        for w in word:
            if w not in tmp:
                tmp[w] = {}
                
            tmp = tmp[w]
        
        tmp['end'] = True
        

    def search(self, word: str) -> bool:
        
        tmp = self.t
        
        for w in word:
            
            if w not in tmp:
                return False
            
            tmp = tmp[w]
        
        return 'end' in tmp
            
        

    def startsWith(self, prefix: str) -> bool:
        
        tmp = self.t
        
        for p in prefix:
            
            if p not in tmp:
                return False
            
            tmp = tmp[p]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)