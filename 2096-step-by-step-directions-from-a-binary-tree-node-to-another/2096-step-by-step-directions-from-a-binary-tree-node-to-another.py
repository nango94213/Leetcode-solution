# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        info = {}
        p_s = set()
        
        ptr = startValue
        
        def dfs(node, parent):
            if node:
                info[node.val] = parent
                dfs(node.left, (node.val, 0))
                dfs(node.right, (node.val, 1))
        dfs(root, (0, 0))
        
        while ptr:
            p_s.add(ptr)
            ptr = info[ptr][0]
        
        res = ''
        while destValue not in p_s:
            par, d = info[destValue]

            if d == 0:
                res = 'L' + res
            else:
                res = 'R' + res
            destValue = par
        
        count = 0
        while startValue != destValue:
            startValue = info[startValue][0]
            count += 1
        
        return count*'U' + res
            
            
        