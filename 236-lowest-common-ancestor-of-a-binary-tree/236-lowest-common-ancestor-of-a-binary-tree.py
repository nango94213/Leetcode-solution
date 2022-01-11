# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent={}
        def dfs(node,par):
            if node:
                node.par = par
                
                dfs(node.left,node)
                dfs(node.right,node)
        
        dfs(root,None)
        
        an=set()
        
        while p:
            an.add(p)
            p=p.par

        while q not in an:
            q=q.par
        
        return q
            
            
        