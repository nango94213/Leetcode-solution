# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        depth = 0
        
        check = root
        
        while check.left :
            depth += 1
            check = check.left
        
        def exist(index, node):
            l, r = 0, 2**depth - 1
            for _ in range(depth):
                mid = (l+r) // 2
                if index <= mid:
                    node = node.left
                    r = mid
                else:
                    node = node.right
                    l = mid + 1
             
            
            return node is not None
                
        
        
        left, right = 0, 2**depth - 1
        
        while left <= right:
            mid = (left+right) // 2
            
            if exist(mid,  root):
                left = mid + 1
            else:
                right = mid - 1
        
        return 2**depth - 1 + left