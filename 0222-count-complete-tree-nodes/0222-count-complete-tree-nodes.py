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
        
        d = -1
        
        p = root
        
        while p:
            p = p.left
            d += 1
     
        def check(index):
            p = root
            l = 0
            r = 2**d - 1
            for _ in range(d):
                mid = (l+r) // 2
                if index <= mid:
                    p = p.left
                    r = mid
                else:
                    l = mid + 1
                    p = p.right
                    
            return p != None
        
        left = 0
        right = 2**d - 1
        
        
        while left <= right:
            mid = (left+right) // 2
            
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return 2**d - 1 + left
            