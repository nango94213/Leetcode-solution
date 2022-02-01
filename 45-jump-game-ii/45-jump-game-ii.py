class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 0
        l,r=0,nums[0]
        jump=1
        while r<len(nums)-1:
            farthest=max([i+nums[i] for i in range(l,r+1)])
            jump+=1
            l,r=r+1,farthest
        return jump
            