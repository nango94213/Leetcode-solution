import random, bisect
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        number = random.random() * self.w[-1]
        return bisect.bisect_left(self.w, number)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()