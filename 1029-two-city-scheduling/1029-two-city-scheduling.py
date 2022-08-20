class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        
        total = 0
        
        n = len(costs) // 2
        
        return sum([cost[0] for cost in costs[:n]]) + sum([cost[1] for cost in costs[n:]])
            
            
            