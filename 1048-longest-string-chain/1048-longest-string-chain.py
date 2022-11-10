class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=len)
        
        dic = {}
        
        for i, w in enumerate(words):
            dic[w] = 1
            
            for j in range(len(w)):
          
                pre = w[:j] + w[j+1:]
            
                if pre in dic:
                    dic[w] = max(dic[w], dic[pre]+1)
       
        return max(dic.values())
                