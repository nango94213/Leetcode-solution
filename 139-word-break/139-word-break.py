class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        dic = set()
        
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dic.add(s[:i+1])
            else:
                for j in range(i):   # s[:i+1] = 'abcd'
                    if s[:j+1] in dic and s[j+1:i+1] in wordDict:
                        dic.add(s[:i+1])
                        break

        return s in dic