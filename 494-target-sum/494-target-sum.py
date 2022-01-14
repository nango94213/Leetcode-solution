class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        seen={}
        def dfs(pool,path):
            if (pool,path) not in seen:
              
                if pool==len(nums):
                    if path==target:
                        return 1
                    else:
                        return 0

                r=dfs(pool+1,path+nums[pool])+dfs(pool+1,path-nums[pool])
                seen[(pool,path)]=r
                return r
   
            
            else:
                return seen[(pool,path)]
            
            
        
        return dfs(0,0)