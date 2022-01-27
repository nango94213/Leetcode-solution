class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dic = {}
        
        res = 0
        
        words = sorted(words, key=len)
        for word in words:
            
            chain = 1
            
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
                
                if pre in dic:
                    
                    chain = max(chain, dic[pre]+1)
            
            dic[word] = chain
            res = max(chain, res)
        
        return res
        
        
        
        