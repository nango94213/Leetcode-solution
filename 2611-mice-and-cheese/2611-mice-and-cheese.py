import heapq
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        
        return sum(reward2) + sum(heapq.nlargest(k, [reward1[i]-reward2[i] for i in range(len(reward1))]))
        