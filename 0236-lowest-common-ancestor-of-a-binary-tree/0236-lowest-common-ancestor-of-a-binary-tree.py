# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p):
            if node:
                node.par = p
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        p_s = set()
        
        while p:
            p_s.add(p)
            p = p.par
        while q not in p_s:
            q = q.par
        return q
        