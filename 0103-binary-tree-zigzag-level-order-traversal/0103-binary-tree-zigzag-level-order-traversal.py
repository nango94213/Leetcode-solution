# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        left = True
        
        while q:
            level = collections.deque()
            for _ in range(len(q)):
                current = q.popleft()
                
                if left:
                    level.append(current.val)
                    
                else:
                    level.appendleft(current.val)
                    
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            left = not left
            res.append(level)
        
        return res
                
            