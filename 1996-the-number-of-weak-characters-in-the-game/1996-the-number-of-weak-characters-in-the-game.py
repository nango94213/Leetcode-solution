class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key = lambda x: (x[0], -x[1]))
        
        stack = []
        count = 0
        
        for v in properties:
            while stack and stack[-1] < v[1]:
                stack.pop()
                count += 1
            stack.append(v[1])
        return count