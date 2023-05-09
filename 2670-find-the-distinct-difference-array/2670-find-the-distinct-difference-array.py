class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        seen = set()
        
        pre = []
        
        for n in nums:
            if not pre:
                pre.append(1)
                seen.add(n)
            else:
                if n in seen:
                    pre.append(pre[-1])
                else:
                    pre.append(pre[-1]+1)
                    seen.add(n)
        res = []
        current = 0
        seen = set()
        n = len(nums)
        for i in range(len(nums)-1, -1, -1):
            res.append(pre[i]-current)
            if nums[i] not in seen:
                current += 1
                seen.add(nums[i])
        return reversed(res)
                
            
        