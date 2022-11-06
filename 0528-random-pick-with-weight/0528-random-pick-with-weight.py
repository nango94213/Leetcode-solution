import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] = w[i-1] + w[i]
        
        self.w = w
        self.total = w[-1]
        

    def pickIndex(self) -> int:
        pick = random.random() * self.total
        return bisect.bisect_left(self.w, pick)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()