class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)
        
        dp = set()
        
        for i in range(len(s)):
            
            if s[:i+1] in word_set:
                dp.add(s[:i+1])
            
            else:
                for j in range(i):
                    if s[:j+1] in dp and s[j+1:i+1] in word_set:
                        dp.add(s[:i+1])
        
        return s in dp