class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties = sorted(properties, key=lambda x: (x[0], -x[1]))
        
        total = 0
        
        check = [x[1] for x in properties]
        
        stack = []
        
        for c in check:
            while stack and stack[-1] < c:
                stack.pop()
                total += 1
            
            stack.append(c)
        
        return total