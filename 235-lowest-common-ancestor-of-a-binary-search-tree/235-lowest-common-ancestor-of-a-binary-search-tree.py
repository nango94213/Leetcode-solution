# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        def dfs(node, parent):
            
            if node:
                
                node.gg = parent
                
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
        
        parents = set()
        
        while p:
            
            parents.add(p)
            p = p.gg
            
        while q not in parents:
            q = q.gg
            
        return q
        
        
        
        
        
        
                