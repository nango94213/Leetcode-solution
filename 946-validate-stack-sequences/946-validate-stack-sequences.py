class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        index = 0
        stack = []
        for i in pushed:
            stack.append(i)
            
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        

        if stack:
            return False
        else:
            return True
                