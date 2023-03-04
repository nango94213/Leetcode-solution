class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = []
        rem = 0
        for n in word:
            n = int(n)
            rem = (rem*10 + n) % m
          
            if rem == 0:
                res.append(1)
            else:
                res.append(0)
        
        return res
        