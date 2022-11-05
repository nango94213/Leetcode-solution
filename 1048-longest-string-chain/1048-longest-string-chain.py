class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dic = {}
        res = 0
        words.sort(key=len)
  
        for word in words:
            dic[word] = 1
            for i in range(len(word)):
                pre = word[:i] + word[i+1:]
               
                if pre in dic:
                    dic[word] = max(dic[word], dic[pre]+1)
            
     
            
  
        return max(dic.values())