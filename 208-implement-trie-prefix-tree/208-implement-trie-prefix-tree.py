class Trie:

    def __init__(self):
        
        self.trie = {}
        

    def insert(self, word: str) -> None:
        t = self.trie
        
        for w in word:
            if w not in t:
                t[w] = {}
            
            t = t[w]
        t['end'] = True
        

    def search(self, word: str) -> bool:
        
        t = self.trie
        
        for w in word:
            if w not in t:
                return False
            t = t[w]
        
        return 'end' in t
        

    def startsWith(self, prefix: str) -> bool:
        
        t = self.trie
        
        for p in prefix:
            if p not in t:
                return False
            t = t[p]
        
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)