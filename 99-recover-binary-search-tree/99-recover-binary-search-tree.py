# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        res = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node)
                dfs(node.right)
        
        dfs(root)
        
        first = None
        second = None
 
        for i in range(len(res)-1):
     
            if res[i].val >= res[i+1].val and not first:
                first = res[i]
                
            
            if res[i].val >= res[i+1].val and first:
                second = res[i+1]

  
        first.val, second.val = second.val, first.val