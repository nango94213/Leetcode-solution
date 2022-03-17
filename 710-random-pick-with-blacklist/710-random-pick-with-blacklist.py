import random
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.dic = {}
        
        self.range = n - len(blacklist)
        self.blacklist = set(blacklist)
        n_black = len(blacklist)
        
        starter = n - n_black
        for b in blacklist:
            if b < (n-n_black):
                while starter in blacklist:
                    starter += 1
                self.dic[b] = starter
                starter += 1
        

    def pick(self) -> int:
        
        number = random.randint(0, self.range-1)
        
        return number if number not in self.blacklist else self.dic[number]
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()