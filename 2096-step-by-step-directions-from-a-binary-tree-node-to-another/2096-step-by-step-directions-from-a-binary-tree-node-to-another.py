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
            
            if node:
                dic[node.val] = parent
                
                dfs(node.left, (node.val, 0))
                dfs(node.right, (node.val, 1))
        
        dfs(root, (-1, -1))
        
        parent_start = set()
        
        tmp = startValue
        
        while tmp != -1:
            parent_start.add(tmp)
            tmp = dic[tmp][0]
        
        tmp = destValue
        
        res = ''
        
        while tmp not in parent_start:
            if dic[tmp][1] == 0:
                res = 'L' + res
            if dic[tmp][1] == 1:
                res = 'R' + res
            
            tmp = dic[tmp][0]
        
        count = 0
        
        while startValue != tmp:
            count += 1
            startValue = dic[startValue][0]
        
        return count*'U' + res
            