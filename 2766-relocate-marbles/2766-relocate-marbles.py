class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        count = Counter()
        
        for n in nums:
            count[n] += 1
        
        for i in range(len(moveFrom)):
            n = count[moveFrom[i]]
            count[moveFrom[i]] -= n
            count[moveTo[i]] += n
        res = []
        
        for k in sorted(count.keys()):
            if count[k] > 0:
                res.append(k)
        
        return res
        