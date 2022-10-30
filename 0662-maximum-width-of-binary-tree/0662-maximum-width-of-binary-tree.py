# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque([(root, 0)])
        res = 1
        while q:
            level = []
            for _ in range(len(q)):
                current, d = q.popleft()
                level.append(d)
                
                if current.left:
                    q.append((current.left, 2*d))
                if current.right:
                    q.append((current.right, 2*d+1))
            
            if len(level) >= 2:
                res = max(res, max(level)-min(level)+1)
        
        return res
                
            
            
        
        
        
        