class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        dp = [1] * len(arr)
        
        
        arr.sort()
        dic = {v: i for i, v in enumerate(arr)}
         
        for i in range(len(arr)):
            for j in range(i):
                
                if arr[i] % arr[j] == 0:
                    right = arr[i]/arr[j]
                    if right in dic:

                            dp[i] += dp[j] * dp[dic[right]]
                            dp[i] %= (10**9+7)
        
        return sum(dp) % (10**9+7)
            
    