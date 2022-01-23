class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []
        for i in pushed:
            stack.append(i)
            
            while stack and stack[-1] == popped[index] and index < len(popped):
                stack.pop()
                index += 1
        
        
        return len(stack) == 0
                