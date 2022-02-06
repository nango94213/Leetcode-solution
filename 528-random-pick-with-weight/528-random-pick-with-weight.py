import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1,len(w)):
            w[i]+=w[i-1]
        self.w=w
        self.total=w[-1]
            
        

    def pickIndex(self) -> int:
        target=random.random()*self.total
        return bisect.bisect_right(self.w,target)
        
        
'''
[1,3,3,1] pick a number, if 
n is greater than 4 and less than 7 we know it's in 
range (4,7) so it's 2


'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


"""import random
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1,len(w)):
            w[i]+=w[i-1]
        self.w=w
            
        

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)),cum_weights=self.w,k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()"""