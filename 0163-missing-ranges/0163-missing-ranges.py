class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        a=[]
        if nums==[]:
            if upper==lower:
                return [str(lower)]
            else:
                return [str(lower)+'->'+str(upper)]
        if nums[0]>lower:
            if nums[0]-1==lower:
                a.append(str(lower))
            else:
                a.append(str(lower)+'->'+str(nums[0]-1))
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==2:
                a.append(str(nums[i]-1))
            elif nums[i]-nums[i-1]>2:
                a.append(str(nums[i-1]+1)+'->'+str(nums[i]-1))
        if upper-nums[-1]==1:
            a.append(str(upper))
        elif upper-nums[-1]>1:
            a.append(str(nums[-1]+1)+'->'+str(upper))
        return a