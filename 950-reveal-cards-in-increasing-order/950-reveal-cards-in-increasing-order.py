import collections
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        
        res = [None] * len(deck)
        
        index = collections.deque(range(len(deck)))
        
        
        for card in deck:
            
            res[index.popleft()] = card
            
            if index:
                
                index.append(index.popleft())
        
        return res
        
        
        