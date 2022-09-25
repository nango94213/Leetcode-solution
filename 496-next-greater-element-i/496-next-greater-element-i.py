import collections
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dic = collections.defaultdict(lambda: -1)
        
        stack = []
        
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            
            stack.append(n)
        
        res = []
        
        for n in nums1:
            res.append(dic[n])
        
        return res