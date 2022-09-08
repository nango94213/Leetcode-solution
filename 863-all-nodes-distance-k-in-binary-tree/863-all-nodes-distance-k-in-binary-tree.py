# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node, par):
            if node:
                node.parent = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
               
        q = deque([(target, 0)])
                    
        seen = set([target])
        
        while q:
            
            
            
            if q[0][1] == k:
                return [n[0].val for n in q]
            
            current, distance = q.popleft()
            
            if current.left and current.left not in seen:
                seen.add(current.left)
                q.append((current.left, distance+1))
                
            if current.right and current.right not in seen:
                seen.add(current.right)
                q.append((current.right, distance+1))
                
            if current.parent and current.parent not in seen:
                seen.add(current.parent)
                q.append((current.parent, distance+1))
        
        return []
        