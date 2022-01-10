# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node,par=None):
            if node:
                node.par=par
                dfs(node.left,node)
                dfs(node.right,node)
        dfs(root)
        q=deque([(target,0)])
        seen={target}
        while(len(q)>0):
            if q[0][1]==k:
                return [n[0].val for n in q]
            
            node,d=q.popleft()
            
    
            if node.left and (node.left not in seen):
                seen.add(node.left)
                q.append((node.left,d+1))
            if node.right and (node.right not in seen):
                seen.add(node.right)
                q.append((node.right,d+1))
            if node.par and (node.par not in seen):
                seen.add(node.par)
                q.append((node.par,d+1))
          

        return []
        