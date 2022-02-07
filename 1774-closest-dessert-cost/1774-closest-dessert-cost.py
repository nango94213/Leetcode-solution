class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        res = float('inf')
        
        def dfs(topping, current_sum):
            nonlocal res

            if abs(current_sum - target) < abs(res - target):
                
                res = current_sum
            
            if abs(current_sum - target) == abs(res - target):
                
                res = min(current_sum, res)
            
            if current_sum > target:
                return
            
            for i in range(len(topping)):
                dfs(topping[i+1:], current_sum)
                dfs(topping[i+1:], current_sum+topping[i])
                dfs(topping[i+1:], current_sum+2*topping[i])
        
        for base in baseCosts:
            dfs(toppingCosts, base)
        
        return res
                
                