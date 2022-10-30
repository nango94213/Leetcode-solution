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
        res = 0
        while q:
            level = []
            start = q[0][1]
            for _ in range(len(q)):
                current, d = q.popleft()
                level.append(d)
                
                if current.left:
                    q.append((current.left, 2*d))
                if current.right:
                    q.append((current.right, 2*d+1))
            
            
            res = max(res, d - start+1)
        
        return res
                
            
            
        
        
        
        