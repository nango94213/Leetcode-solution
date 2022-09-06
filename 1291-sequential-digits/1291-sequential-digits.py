class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = []
        
        
        def dfs(number):
            
            if low <= number <= high:
                res.append(number)
            
            if number > high:
                return
            
            if number % 10 == 9:
                return
            
            dfs(number*10+(number%10+1))
        
        
        for i in range(1, 9):
            dfs(i)
        
        return sorted(res)