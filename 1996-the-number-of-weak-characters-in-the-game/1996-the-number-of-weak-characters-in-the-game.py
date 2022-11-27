class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        
        res = 0
        
        check = [i[1] for i in properties]
        
        stack = []
        
        for c in check:
            while stack and stack[-1] < c:
                res += 1
                stack.pop()
            
            stack.append(c)
        
        return res