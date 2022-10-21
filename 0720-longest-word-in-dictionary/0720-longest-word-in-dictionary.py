class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        seen = set([''])
        res = ''
        words.sort()
        
        for word in words:
            if word[:-1] in seen:
                seen.add(word)
                
                if len(word) > len(res):
                    res = word
        
        return res