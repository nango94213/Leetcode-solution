class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(pool,path):
            if len(path) == len(nums):
                output.append(path)
            for i in range(len(pool)):
                backtracking(pool[:i]+pool[i+1:],path+[pool[i]])
                
            
        output=[]
        backtracking(nums,[])
        return output