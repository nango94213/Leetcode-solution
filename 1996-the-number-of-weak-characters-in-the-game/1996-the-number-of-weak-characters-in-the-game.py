class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties = sorted(properties, key=lambda x: (x[0], -x[1]))
        
        stack = []
        res = 0
        
        for v in [i[1] for i in properties]:
            
            while stack and stack[-1] < v:
                stack.pop()
                res += 1
            
            stack.append(v)
        
        return res