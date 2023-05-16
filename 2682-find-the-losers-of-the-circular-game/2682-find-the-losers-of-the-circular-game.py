class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        current = 1
        seen = set()
        i = 1
        while current not in seen:
            seen.add(current)
            
            current = (current + i * k) % n
            if current == 0:
                current = n
            i += 1
        res = []
  
        for i in range(1, n+1):
            if i not in seen:
                res.append(i)
        return res