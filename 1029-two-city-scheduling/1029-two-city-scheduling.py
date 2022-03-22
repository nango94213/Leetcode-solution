class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs = sorted(costs, key=lambda x: x[0]-x[1])
        
        total = 0
        n = len(costs) // 2
        
        for c in costs:
            if n:
                total += c[0]
                n -= 1
            else:
                total += c[1]
        
        return total
        
        