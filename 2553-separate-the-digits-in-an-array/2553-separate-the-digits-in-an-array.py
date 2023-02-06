class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        
        for n in nums:
            res += list(str(n))
        
        return map(int, res)