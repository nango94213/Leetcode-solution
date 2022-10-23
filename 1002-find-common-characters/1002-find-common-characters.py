class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        count1 = Counter(words[0])
        
        for w in words[1:]:
            count2 = Counter(w)
            
            for key in count1:
                count1[key] = min(count2[key], count1[key])
          
        
        res = []
        for k, v in count1.items():
            res += [k] * v
        return res
        