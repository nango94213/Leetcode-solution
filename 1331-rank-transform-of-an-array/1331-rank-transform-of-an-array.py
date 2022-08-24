class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        old = deepcopy(arr)
        
        arr.sort()
        
        dic = {}
        
        res = []
        
        position = 0
        
        for number in arr:
            
            if number not in dic:
                position += 1
                dic[number] = position
       
        for number in old:
            res.append(dic[number])
        
        return res
        
        