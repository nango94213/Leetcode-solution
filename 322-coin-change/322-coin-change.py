class Solution(object):
    def coinChange(self, coins, amount):
        '''dic=[float('inf')]*(amount+1)
        dic[0]=0
        for i in range(1,len(dic)):
            for j in coins:
                if amount-j>=0:
                    dic[i]=min(dic[i],dic[i-j]+1)
        return dic[amount] if dic[amount]!=float('inf') else -1
        '''
        
        dic=[float('inf')]*(amount+1)
        dic[0]=0
        for i in coins:
            for j in range(i,amount+1):
                dic[j]=min(dic[j],dic[j-i]+1)
        return dic[amount] if dic[amount]!=float('inf') else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        
       
       
       
        dp=[-1 for i in range(amount+1)]
        dp[0]=0
        for i in range(1,len(dp)):
            if i in coins:
                dp[i]=1
            else:
                minn=amount+1
                for j in coins:
                    if i-j>=0:
                        if dp[i-j]!=-1:
                            minn=min(minn,dp[i-j]+1)
                if minn!=amount+1:
                    dp[i]=minn
        return dp[amount]    
       
        """
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """if amount==0:
            return 0
        
        dp=[-1 for i in range(amount)]
        
        
        for i in range(1,amount+1):
            if i in coins:
                dp[i-1]=1
            else:
                for j in coins:
                    if j<i and dp[i-j-1]!=-1:
                        if dp[i-1]==-1:
                            dp[i-1]=amount
                        dp[i-1]=min(dp[i-1],dp[i-j-1]+1)
                            
        return dp[amount-1]"""