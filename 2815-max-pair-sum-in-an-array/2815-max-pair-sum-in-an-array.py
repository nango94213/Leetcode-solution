import collections
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = collections.defaultdict(list)
        
        def find(x):
            return int(max(list(str(x))))
        
        for n in nums:
            m = find(n)
            dic[m].append(n)
        
        res = -1
        for k in dic:
            if len(dic[k]) >= 2:
                good = max(dic[k])
                
                second = 0
                t = 0
                for n in dic[k]:
                    if n == good:
                        t += 1
                    if n < good:
                        second = max(second, n)
                if t > 1:
                    second = good
                res = max(res, good + second)
        
        return res