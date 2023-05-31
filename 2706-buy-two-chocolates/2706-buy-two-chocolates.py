class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = float('inf')
        b = float('inf')
        t = 0
        
        for i, p in enumerate(prices):
            if p < a:
                a = p
                t = i
        for i, p in enumerate(prices):
            if p < b and i != t:
                b = p
        res = money - a - b
        return res if res >= 0 else money
        