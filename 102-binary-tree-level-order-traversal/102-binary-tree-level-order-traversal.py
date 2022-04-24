# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        
        q = deque()
        
        q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                
                current = q.popleft()
                
                level.append(current.val)
                
                if  current.left:
                    q.append(current.left)
                
                if current.right:
                    q.append(current.right)
            
            res.append(level)
        
        return res
            
                
            
            