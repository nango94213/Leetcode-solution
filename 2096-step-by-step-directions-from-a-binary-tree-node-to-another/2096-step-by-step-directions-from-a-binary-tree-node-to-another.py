# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        dic = {}
        
        def dfs(node, parent):
            
            if not node:
                return
            
            dic[node.val] = parent
            
            dfs(node.left, (node.val, 0))
            dfs(node.right, (node.val, 1))
        
        dfs(root, (-1, -1))
        
        p_parent = set()
        
        tmp = startValue
     
        while tmp != -1:
            p_parent.add(tmp)
            
            tmp = dic[tmp][0]
        
        
        
        final = ''
        
        while destValue not in p_parent:
            
            if dic[destValue][1] == 0:
                final = 'L' + final
            else:
                final = 'R' + final
            destValue = dic[destValue][0]

        
        
        count1 = 0
        while startValue != destValue:
            count1 += 1
            startValue = dic[startValue][0]
        
        return count1*'U' + final