class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        dic = {}
        
        for p in pairs:
            
            dic[p[0]] = set(preferences[p[0]][:preferences[p[0]].index(p[1])])
            dic[p[1]] = set(preferences[p[1]][:preferences[p[1]].index(p[0])])
            
            
        res = 0
        
        for i in dic:
            
            for j in dic[i]:
                
                if i in dic[j]:
                    
                    res += 1
                    break
        
        return res