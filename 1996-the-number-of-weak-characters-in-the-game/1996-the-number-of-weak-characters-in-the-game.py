class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties = sorted(properties, key=lambda x: (x[0], -x[1]))
        
        total = 0
        

        
        stack = []
        
        for c in [i[1] for i in properties]:
            while stack and stack[-1] < c:
                stack.pop()
                total += 1
            
            stack.append(c)
        
        return total