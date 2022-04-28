class WordDictionary:

    def __init__(self):
        self.t = {}

    def addWord(self, word: str) -> None:
        tmp = self.t
        
        for w in word:
            if w not in tmp:
                tmp[w] = {}
                
            tmp = tmp[w]
        
        tmp['end'] = True


    def search(self, word: str) -> bool:
        
        def s(word, node):
            for i,v in enumerate(word):
                
                if v == '.':
                    for x in node:
                        if x != 'end' and s(word[i+1:], node[x]):
                            return True
           
                
                if v not in node:
                    return False
                
                node = node[v]
            
            return 'end' in node
    
        
        return s(word, self.t)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)