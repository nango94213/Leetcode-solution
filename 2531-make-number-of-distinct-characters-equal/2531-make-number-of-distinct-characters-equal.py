class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        
        t1 = list(count1.keys())
        t2 = list(count2.keys())
        for a in t1:
            for b in t2:
                c1 = count1.copy()
                c2 = count2.copy()
                c1[a] -= 1
                c2[a] += 1
                c2[b] -= 1
                c1[b] += 1
                
                if c1[a] == 0:
                    del c1[a]
                if c2[b] == 0:
                    del c2[b]
              
                if len(c1) == len(c2):
                    return True
        
        return False
                
        