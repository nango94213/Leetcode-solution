class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = list(Counter(nums).items())
        
        count.sort(key = lambda x: x[1], reverse=True)
        print(count)
        res = [[] for _ in range (count[0][1])]
        
        for n in count:
            for i in range(n[1]):
                res[i].append(n[0])
        
        return res
        
        
        
        
        