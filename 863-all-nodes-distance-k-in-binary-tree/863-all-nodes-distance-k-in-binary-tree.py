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
               
        q = deque([target])
                    
        seen = set([target])
        
        d = 0
        res = []

        while q and d <= k:
            
            for _ in range(len(q)):
                current = q.popleft()
                print(d)
                if d == k:
                    res.append(current.val)
                    continue
            
                if current.left and current.left not in seen:
                    seen.add(current.left)
                    q.append(current.left)
                
                if current.right and current.right not in seen:
                    seen.add(current.right)
                    q.append(current.right)
                
                if current.parent and current.parent not in seen:
                    seen.add(current.parent)
                    q.append(current.parent)
            d += 1

        return res
        