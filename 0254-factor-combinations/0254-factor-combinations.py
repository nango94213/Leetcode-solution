class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        nums = [x for x in range(2,n//2+1) if n % x == 0]
        result = []
        def dfs(nums,index,path,target):
            if target < 1: return
            if target == 1 and path:
                result.append(path)
                return
            for i in range(index,len(nums)):
                if target % nums[i] == 0:
                    dfs(nums,i,path+[nums[i]],target//nums[i])
        dfs(nums,0,[],n)
        return result
            
            