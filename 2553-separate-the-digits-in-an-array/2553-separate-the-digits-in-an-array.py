class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        
        for n in nums:
            tmp = []
            while n:
                tmp.append(n%10)
                n //= 10
            for i in range(len(tmp)-1, -1, -1):
                res.append(tmp[i])
        
        return res