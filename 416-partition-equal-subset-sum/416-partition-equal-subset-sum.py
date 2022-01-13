class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        
        sums=set([0])
        
        for n in nums:
            temp=[]
            for i in sums:
                if n+i==target:
                    return True
                
                if n+i<target:
                    temp.append(n+i)
            sums.update(temp)
        return False
                    
        