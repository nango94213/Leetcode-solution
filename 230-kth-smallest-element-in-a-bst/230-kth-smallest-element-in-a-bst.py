# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        h = []
        
        def dfs(node):
            
            if node:
                heapq.heappush(h, -node.val)
                
                if len(h) > k:
                    heapq.heappop(h)
          
                
                dfs(node.left)
                dfs(node.right)
        
        
        dfs(root)
    
        return -h[0]
        
        