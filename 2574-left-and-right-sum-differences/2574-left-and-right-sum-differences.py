class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        n = len(nums)
        for i in range(len(nums)-1):
            left.append(left[-1]+nums[i])
        ans = collections.deque()
        
        now = 0
        for i in range(len(nums)-1, -1, -1):
            ans.appendleft(abs(left[i]-now))
            now += nums[i]
        return ans