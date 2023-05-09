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
        back = [0]
        seen = set()
        for i in range(len(nums)-1, 0, -1):
            if len(back) == 1:
                back.append(1)
                seen.add(nums[i])
            else:
                if nums[i] in seen:
                    back.append(back[-1])
                else:
                    back.append(back[-1]+1)
                    seen.add(nums[i])
        res = []
        
        for i in range(len(pre)):
            res.append(pre[i]-back[-i-1])
        return res
                
            
        