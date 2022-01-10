class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def ksum(nums,target,k,path):
            if len(nums)==0 or nums[0]*k>target or nums[-1]*k<target:
                return
            if k==2:
                for subset in twosum(nums, target):
                    res.append(path + subset)
            for i in range(len(nums)):
                if i==0 or nums[i-1]!=nums[i]:
                     ksum(nums[i+1:],target-nums[i],k-1,path + [nums[i]])
                        

        
        def twosum(numss,target):
            ans=[]
            l=0
            r=len(numss)-1
            while l<r:
                two_sum=numss[l]+numss[r]
                if two_sum==target:
                    ans.append([numss[l],numss[r]])
                    l+=1
                    r-=1
                    while l<r and numss[l]==numss[l-1]:
                        l+=1
                    while l<r and numss[r]==numss[r+1]:
                        r-=1
                elif two_sum>target:
                    r-=1
                else:
                    l+=1
            return ans
        
        
        nums.sort()
        ksum(nums,target,4,[])
        
        return res